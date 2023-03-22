from config import constants


class Config:
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = constants.SQLALCHEMY_DATABASE_URI
    JWT_SECRET_KEY = constants.JWT_SECRET_KEY
    SECRET_KEY = constants.SECRET_KEY
