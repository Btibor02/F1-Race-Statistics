from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import login_manager

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    fav_driver_1 = db.Column(db.String(5), nullable=True)
    fav_driver_2 = db.Column(db.String(5), nullable=True)
    fav_team = db.Column(db.String(5), nullable=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class DriverStanding(db.Model):
    __tablename__ = 'driver_standings'

    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.Integer, nullable=False)
    round = db.Column(db.Integer, nullable=False)
    driver_id = db.Column(db.String(20), nullable=False)
    position = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    wins = db.Column(db.Integer, nullable=False)
    
    __table_args__ = (db.UniqueConstraint('driver_id', name='uq_driver_standing'),)
