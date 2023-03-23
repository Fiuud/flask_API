from api.home import home_route
from api.login import login_route
from api.qr import qr_route
from api.student import student_route


def register_routes(app):
    app.register_blueprint(student_route)
    app.register_blueprint(login_route)
    app.register_blueprint(qr_route)
    app.register_blueprint(home_route)
