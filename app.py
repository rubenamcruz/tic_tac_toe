from flask import Flask, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from db.entities import db, User
from db.user_management import validate_login, add_user
from services.forms import LoginForm, RegisterForm
from services.login_manager import login_manager, LoginUser

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config.from_object('settings')

db.init_app(app)
db.app = app
db.create_all()

login_manager.init_app(app)


# login manager callbacks

@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter_by(username=user_id).first()
    if user is None:
        return
    return LoginUser(user.username)

@login_manager.request_loader
def header_loader(request):
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    if user is None:
        return
    return LoginUser(username)


# view callbacks

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play')
def play_locally():
    return render_template('local/game.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', message='', form=form)
    if form.validate_on_submit():
        is_valid, statement = validate_login(form.username.data, form.password.data)
        if is_valid:
            loguser=LoginUser(form.username.data)
            login_user(loguser)
            return redirect(url_for("home"))
        else:
            return render_template('login.html', message=statement, form=form)
    else:
        return render_template('login.html', message='', form=form)


@app.route('/register', methods=['GET', 'POST'])
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


@app.route('/logout', )
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.errorhandler(401)
@app.errorhandler(403)
def unauthorized(e):
    return 'unauthorized'

if __name__ == "__main__":
    app.run()
