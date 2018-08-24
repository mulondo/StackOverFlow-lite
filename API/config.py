"""contains all configuration"""
import os


class Config:
    """
    This is the parent configuration class to be inherited from
    """
    DEBUG = False
    SECRET = os.getenv('SECRET')
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
    """
    development environment configuration 
    """
    DEBUG = True
    SECRET = 'efa27950565790fbaecfb5fb64b84a6a7c48d06d'
    SECRET_KEY = 'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'


class TestingConfig(Config):
    """
    The configuration for testing
    """
    DEBUG = True
    SECRET = 'efa27950565790fbaecfb5fb64b84a6a7c48d06d'
    TESTING = True
    SECRET_KEY = 'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'


class ProductionConfig(Config):
    """
    more configuration for Production
    """
    DEBUG = False
    TESTING = False
