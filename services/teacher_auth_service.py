from flask import redirect, url_for, flash, render_template, jsonify
from flask_login import logout_user, login_user, current_user
from werkzeug.security import check_password_hash

from models.controllers import TeacherAuthController
from utils import LoginForm
from utils import RegisterForm


def teacher_login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))

    form = LoginForm()
    if form.validate_on_submit():

        email = form.email.data
        password = form.password.data
        remember = form.remember.data

        teacher_auth = TeacherAuthController.get_teacher_auth(email=email)

        if teacher_auth and check_password_hash(teacher_auth.password_hash, password):
            login_user(teacher_auth, remember=remember)
            return redirect(url_for('home.index'))
        else:
            flash('Неверный логин или пароль', 'danger')
            return redirect(url_for('.teacher_login'))
    return render_template('auth/teacher_login.html', form=form)


def teacher_reg():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))

    form = RegisterForm()
    if form.validate_on_submit():
        data = {
            "email": form.email.data,
            "password": form.password.data,
            "last_name": form.last_name.data,
            "first_name": form.first_name.data,
            "middle_name": form.middle_name.data
        }
        TeacherAuthController.create_teacher_auth(data)
        flash('Аккаунта успешно создан', 'success')
        return redirect(url_for('.teacher_login'))
    return render_template('auth/teacher_reg.html', form=form)


def logout_teacher():
    logout_user()
    flash('Вы вышли из аккаунта', 'success')
    return redirect(url_for('teacher_auth.teacher_login'))
