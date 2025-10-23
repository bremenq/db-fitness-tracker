import os

class Config:
    """Base configuration class"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fittrack-secret-key-change-in-production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Database configuration for ClamV server
    # TODO: Update these with actual ClamV credentials
    DB_USERNAME = os.environ.get('DB_USERNAME') or 'your_username'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'your_password'
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_NAME = os.environ.get('DB_NAME') or 'fittrack_pro'
    
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration for ClamV server"""
    DEBUG = False
    
    # Override with production settings if needed
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://prod_user:prod_pass@localhost/fittrack_pro'

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
