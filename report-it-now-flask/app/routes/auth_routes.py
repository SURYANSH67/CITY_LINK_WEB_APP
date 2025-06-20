from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user

from ..forms import LoginForm, RegistrationForm, PublicLoginForm
from ..models import User
from .. import db, bcrypt

auth_bp = Blueprint(
    'auth', __name__,
    template_folder='../templates', # Point to parent templates dir
)

# === OFFICIAL (ADMIN) AUTHENTICATION ===
@auth_bp.route('/official/login', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user and user.check_password(form.password.data) and user.role in ['Admin', 'Official']:
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Login unsuccessful. Please check credentials or ensure you have official access.', 'danger')
            
    return render_template('admin/login.html', title='Official Login', form=form)


# === PUBLIC (CITIZEN) AUTHENTICATION ===
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Create user with the default 'Citizen' role
        user = User(name=form.name.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('auth.public_login'))
    return render_template('public/register.html', title='Register', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def public_login():
    if current_user.is_authenticated:
        return redirect(url_for('main.account'))
    form = PublicLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data) and user.role == 'Citizen':
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            flash('You have been successfully logged in.', 'success')
            return redirect(next_page or url_for('auth.account'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('public/login.html', title='Login', form=form)


@auth_bp.route('/account')
@login_required
def account():
    # Ensure this page is only for Citizens
    if current_user.role != 'Citizen':
        return redirect(url_for('admin.dashboard'))
        
    # The backref makes this easy: get all complaints reported by the current user
    complaints = sorted(current_user.reported_complaints, key=lambda c: c.created_at, reverse=True)
    return render_template('public/account.html', title='My Account', complaints=complaints)


# === UNIVERSAL LOGOUT ===
@auth_bp.route('/logout')
@login_required
def logout():
    # Check the user's role to redirect them to the appropriate login page
    is_official = current_user.role in ['Admin', 'Official']
    logout_user()
    flash('You have been successfully logged out.', 'info')
    if is_official:
        return redirect(url_for('auth.admin_login'))
    else:
        return redirect(url_for('auth.public_login'))