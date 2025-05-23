from flask import Blueprint, render_template, redirect, url_for, flash, render_template, request, abort
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, RegistrationForm, PasswordResetForm, ProfileForm, ChangePasswordForm
from .models import User
from functools import wraps
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/race_details')
def race_details():
    return render_template('race_details.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)

@bp.route('/reset-password', methods=['GET', 'POST'])
def reset_password():
    form = PasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            new_password = form.new_password.data
            user.set_password(new_password)
            db.session.commit()
            flash('Your password has been updated!')
            return redirect(url_for('main.login'))
        else:
            flash('Email not found')
    return render_template('reset_password.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.login'))

@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()

    if form.validate_on_submit():
        if form.username.data != current_user.username:
            existing_user = User.query.filter_by(username=form.username.data).first()
            if existing_user:
                flash('Username already exists. Please choose a different one.')
                return redirect(url_for('main.profile'))
        current_user.username = form.username.data

        if form.email.data != current_user.email:
            existing_email = User.query.filter_by(email=form.email.data).first()
            if existing_email:
                flash('Email already exists. Please choose a different one.')
                return redirect(url_for('main.profile'))
        current_user.email = form.email.data

        if form.fav_driver_1.data == form.fav_driver_2.data:
            flash('Please select two different drivers.')
            return redirect(url_for('main.profile'))

        current_user.fav_driver_1 = form.fav_driver_1.data
        current_user.fav_driver_2 = form.fav_driver_2.data
        current_user.fav_team = form.fav_team.data

        db.session.commit()
        flash('Your profile has been updated!')
        return redirect(url_for('main.profile')) 

    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.fav_driver_1.data = current_user.fav_driver_1 or 'Lando Norris'
        form.fav_driver_2.data = current_user.fav_driver_2 or 'Yuki Tsunoda'
        form.fav_team.data = current_user.fav_team or 'McLaren'

    return render_template('profile.html', form=form, user=current_user)

@bp.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()

    if form.validate_on_submit():
        if not check_password_hash(current_user.password_hash, form.old_password.data):
            flash('Old password is incorrect')
            return redirect(url_for('main.change_password'))

        current_user.password_hash = generate_password_hash(form.new_password.data)
        db.session.commit()

        flash('Your password has been updated!')
        return redirect(url_for('main.profile'))
       
    return render_template('change_password.html', form=form)


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.is_admin == False:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/admin')
@admin_required
def admin_panel():
    users = User.query.all()
    return render_template('admin.html', users=users)

@bp.route('/delete_user/<int:user_id>', methods=['POST'])
@admin_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if user.is_admin:
        flash('You cannot delete an admin user.')
        return redirect(url_for('main.admin_panel'))
    if user:
        db.session.delete(user)
        db.session.commit()
        flash(f'User {user.username} has been deleted.')
    else:
        flash('User not found.')
    return redirect(url_for('main.admin_panel'))