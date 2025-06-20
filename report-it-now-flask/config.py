import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Set Flask configuration variables."""
    
    # General Config
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_APP = 'run.py'

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False # Set to True for debugging SQL queries
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # File Uploads
    UPLOAD_FOLDER = os.path.join(basedir, 'app/static/uploads')
    
    # Mail Server Configuration
# Mail Server Configuration
MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'YOUR_EMAIL_HERE'
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'YOUR_PASSWORD_HERE'
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'YOUR_SENDER_EMAIL_HERE'
GOOGLE_MAPS_API_KEY = os.environ.get('GOOGLE_MAPS_API_KEY')