from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
import os

login_manager = LoginManager()
login_manager.login_view = 'main.login'
db = SQLAlchemy()

def create_app():
    basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    templates_path = os.path.join(basedir, 'frontend', 'templates')
    app = Flask(__name__, template_folder=templates_path)
    app.config.from_object(Config)

    from app.models import User
    
    db.init_app(app)
    login_manager.init_app(app)

    from .routes import bp
    app.register_blueprint(bp)

    from .api_routes import api_bp
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()

        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', email='admin@example.com', is_admin=True)
            admin.set_password('Admin123!')
            db.session.add(admin)

        for i in range(1, 6):
            username = f'user{i}'
            email = f'{username}@example.com'
            if not User.query.filter_by(username=username).first():
                user = User(username=username, email=email, is_admin=False)
                user.set_password('User123!')
                db.session.add(user)

        db.session.commit()

    return app