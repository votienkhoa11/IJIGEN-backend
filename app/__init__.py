from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

app = Flask(__name__)
db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()

def create_app(config_class = Config):

    app.config.from_object(Config)
    from app.guests.routes import guests
    app.register_blueprint(guests)

    mail.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)

    return app