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

class Driver(db.Model):
    __tablename__ = 'drivers'

    driver_id = db.Column(db.String(20), primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    nationality = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(5), nullable=False)

class Team(db.Model):
    __tablename__ = 'teams'

    team_id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nationality = db.Column(db.String(50), nullable=False)

class DriverStanding(db.Model):
    __tablename__ = 'driver_standings'

    driver_id = db.Column(db.String(20), nullable=False, primary_key=True)
    season = db.Column(db.Integer, nullable=False)
    round = db.Column(db.Integer, nullable=False)
    position = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    wins = db.Column(db.Integer, nullable=False)

class TeamStanding(db.Model):
    __tablename__ = 'team_standings'

    team_id = db.Column(db.String(20), nullable=False, primary_key=True)
    season = db.Column(db.Integer, nullable=False)
    round = db.Column(db.Integer, nullable=False)
    position = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)
    wins = db.Column(db.Integer, nullable=False)
    
