import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = db if (db := os.getenv('DATABASE_URL')) else 'postgresql+psycopg2://postgres:root@localhost:5432/test'


class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False

