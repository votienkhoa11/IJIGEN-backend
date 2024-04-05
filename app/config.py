import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/ijigen_db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'lovemaki1904@gmail.com'
    MAIL_PASSWORD = 'htlq mqgy ygbh nnel'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True