from flask_login import LoginManager, UserMixin

login_manager = LoginManager()


class LoginUser(UserMixin):
    def __init__(self, username):
        self.id = username

