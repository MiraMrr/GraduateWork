from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bulletin_board.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    
    db.init_app(app)

    with app.app_context():
        from . import routes
        routes.register_routes(app)  # Вызов функции регистрации маршрутов
        db.create_all()

    return app
