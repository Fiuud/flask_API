from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import declarative_base

engine = None
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
base = declarative_base()


# Инициализация базы данных
def init_db(app):
    global engine
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=False)
    db_session.configure(bind=engine)


def shutdown_session(exception=None):
    db_session.remove()
