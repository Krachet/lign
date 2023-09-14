from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from Website import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Log in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('WRONG!!!', category='error')
        else:
            flash('user not exist', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('email already taken', category='success')
        elif len(email) < 4:
            flash('Email too short', category='error')
        elif len(firstname) < 2:
            flash('Not a valid name', category='error')
        elif len(password1) < 8:
            flash('ngan nhu chim may y', category='error')
        elif password2 != password1:
            flash('viet lai cung khong xong', category='error')
        else:
            new_user = User(email=email, first_name=firstname, password=generate_password_hash(
                password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('chuc mung cuoi cung m cung thanh cong', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)
