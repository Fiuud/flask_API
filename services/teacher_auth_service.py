from flask import jsonify, redirect, url_for, request, flash, render_template, abort
from flask_login import logout_user, login_user

from extensions.database_extension import db_session
from models import TeacherAuth
from models.controllers import TeacherAuthController


def teacher_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        remember = True if request.form.get('remember') else False
        print(email, password, remember, request.form.get('remember'))

        teacher_auth = TeacherAuthController.get_teacher_auth(email=email, password=password)
        print(teacher_auth)
        if teacher_auth:
            login_user(teacher_auth, remember=remember)
            return redirect(url_for('home.index'))
        else:
            flash('Неправильный логин или пароль', 'danger')
            return redirect(url_for('teacher_auth.teacher_login'))
    return render_template('auth/teacher_login.html')


def logout_teacher():
    logout_user()
    return redirect(url_for('teacher_auth.teacher_login'))
