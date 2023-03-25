from flask_login import LoginManager

from extensions.database_extension import db_session
from models import TeacherAuth

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return db_session.query(TeacherAuth).get(user_id)
