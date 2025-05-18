from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email, Length, Regexp
from .models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
        Length(min=8, message='Password must be at least 8 characters long'),
        Regexp('^(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$', message='Password must contain at least one special character')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists. Please choose a different one.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists. Please choose a different one.')


class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    new_password = PasswordField('New Password', validators=[DataRequired(),
        Length(min=8, message='Password must be at least 8 characters long'),
        Regexp('^(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$', message='Password must contain at least one special character')])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Reset Password')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(),
        Length(min=8, message='Password must be at least 8 characters long'),
        Regexp('^(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$', message='Password must contain at least one special character')])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')

F1_DRIVERS = [
    ('oscar_piastri', 'Oscar Piastri'),
    ('lando_norris', 'Lando Norris'),
    ('lewis_hamilton', 'Lewis Hamilton'),
    ('george_russell', 'George Russell'),
    ('charles_leclerc', 'Charles Leclerc'),
    ('carlos_sainz', 'Carlos Sainz'),
    ('max_verstappen', 'Max Verstappen'),
    ('kimi_antonelli', 'Kimi Antonelli'),
    ('lance_stroll', 'Lance Stroll'),
    ('fernando_alonso', 'Fernando Alonso'),
    ('alex_albon', 'Alexander Albon'),
    ('esteban_ocon', 'Esteban Ocon'),
    ('pierre_gasly', 'Pierre Gasly'),
    ('yuki_tsunoda', 'Yuki Tsunoda'),
    ('nico_hulkenberg', 'Nico Hulkenberg'),
    ('oliver_bearman', 'Oliver Bearman'),
    ('isack_hadjar', 'Isack Hadjar'),
    ('liam_lawson', 'Liam Lawson'),
    ('jack_doohan', 'Jack Doohan'),
    ('gabriel_bortoleto', 'Gabriel Bortoleto'),
    ('franco_colapinto', 'Franco Colapinto'),
]

F1_TEAMS = [
    ('mclaren', 'McLaren'),
    ('mercedes', 'Mercedes'),
    ('ferrari', 'Ferrari'),
    ('red_bull', 'Red Bull Racing'),
    ('aston_martin', 'Aston Martin'),
    ('alpine', 'Alpine'),
    ('williams', 'Williams'),
    ('haas', 'Haas F1 Team'),
    ('racing_bulls', 'Racing Bulls'),
    ('kick_sauber', 'Kick Sauber'),
]
    


class ProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    fav_driver_1 = SelectField('Favorite Driver 1', choices=F1_DRIVERS, validators=[DataRequired()])
    fav_driver_2 = SelectField('Favorite Driver 2', choices=F1_DRIVERS, validators=[DataRequired()])
    fav_team = SelectField('Favorite Team', choices=F1_TEAMS, validators=[DataRequired()])
    submit = SubmitField('Update Profile')