from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

db = SQLAlchemy()

app.config['FLASK_DEBUG'] = 1
app.config['SECRET_KEY'] = 'rtdpWrc3e7XAkE4Lg7ocem0L7ugwA76y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db.init_app(app)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)



if __name__ == "__main__":
    app.run()