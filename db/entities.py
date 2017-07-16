from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'user'
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(70))
    score = db.Column(db.INTEGER)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.score = 0

    def change_password(self, new_password):
        self.password = new_password

