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

class ProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    fav_driver_1 = SelectField('Favorite Driver 1', choices=[('dri1', 'Driver 1'), ('dri2', 'Driver 2'), ('dri3', 'Driver 3')], validators=[DataRequired()])
    fav_driver_2 = SelectField('Favorite Driver 2', choices=[('dri1', 'Driver 1'), ('dri2', 'Driver 2'), ('dri3', 'Driver 3')], validators=[DataRequired()])
    fav_team = SelectField('Favorite Team', choices=[('team1', 'Team 1'), ('team2', 'Team 2'), ('team3', 'Team 3')], validators=[DataRequired()])
    submit = SubmitField('Update Profile')