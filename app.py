from flask import Flask, render_template, request, redirect, url_for

from db.entities import db, User
from db.user_management import validate_login, add_user
from services.forms import LoginForm, RegisterForm

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object('settings')

db.init_app(app)
db.app = app
db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/play")
def play_locally():
    return render_template('local/game.html')


@app.route("/login", methods=['GET', 'POST'])
def login_user():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', message='', form=form)
    if form.validate_on_submit():
        is_valid, statement = validate_login(form.username.data, form.password.data)
        if is_valid:
            return redirect(url_for("index"))
        else:
            return render_template('login.html', message=statement, form=form)
    else:
        return render_template('login.html', message='', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register_user():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', message='', form=form)
    elif form.validate_on_submit():
        if form.password.data != form.repeat_password.data:
            return render_template('register.html', message="Passwords don't match", form=form)
        elif add_user(form.username.data, form.password.data):
            return redirect(url_for("index"))
        else:
            return render_template('register.html', message='Username already exists!', form=form)
    else:
        return render_template('register.html', message='', form=form)


if __name__ == "__main__":
    app.run()
