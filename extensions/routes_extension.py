from views.home import home_route
from views.scanner_login import scanner_login_route
from views.qr import qr_route
from views.student import student_route
from views.teacher_login import teacher_auth_route


def register_routes(app):
    app.register_blueprint(student_route)
    app.register_blueprint(scanner_login_route)
    app.register_blueprint(qr_route)
    app.register_blueprint(home_route)
    app.register_blueprint(teacher_auth_route)
