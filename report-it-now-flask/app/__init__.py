import os
import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail

from config import Config
from .manual_config import load_config_from_env_file
from .services.email_service import email_sender

# 1. Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
csrf = CSRFProtect()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = 'auth.admin_login'
login_manager.login_message = 'You must be logged in to access this page.'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    """Application-factory pattern."""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config_class)
    env_path = os.path.join(os.path.dirname(app.root_path), '.env')
    load_config_from_env_file(app, env_path)

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    email_sender.init_app(app, mail)

    # We need to import the User model for the loader
    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # --- THIS IS THE CORRECTED PART ---
    # The CLI command is defined here, directly on the app object.
    # It is NOT inside the 'with app.app_context()' block.
    @app.cli.command("create-user")
    @click.argument("name")
    @click.argument("email")
    @click.argument("password")
    @click.option('--role', default='Official', help="Role: Admin, Official, or Citizen")
    def create_user_command(name, email, password, role):
        """Creates a new user with a specified role."""
        # The app context is needed for database operations
        with app.app_context():
            if User.query.filter_by(email=email).first():
                print(f"Error: User with email {email} already exists.")
                return

            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(
                name=name,
                email=email,
                password_hash=hashed_password,
                role=role
            )
            db.session.add(new_user)
            db.session.commit()
            print(f"User '{name}' with role '{role}' created successfully.")
    # --- END OF CORRECTION ---

    # Import and Register Blueprints
    from .routes.main_routes import main_bp
    from .routes.admin_routes import admin_bp
    from .routes.auth_routes import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app