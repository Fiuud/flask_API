import os

import rsa
from dotenv import load_dotenv

load_dotenv()


class Config:
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    AUDIENCE_PASS = os.getenv('AUDIENCE_PASS')
    PUBLIC_KEY = os.getenv("PUBLIC_KEY")
    PRIVATE_KEY = rsa.PrivateKey.load_pkcs1(os.getenv("PRIVATE_KEY").encode('utf-8'))
