"""
runs the application
"""
from flask import Flask
from config import DevelopmentConfig, ProductionConfig
from app.modal import *
from app.views import *


class Server:
    """Create flask object to start the server"""

    @staticmethod
    def create_app(config=None):
        """performs configurations"""
        app = Flask(__name__)
        app.config.update(config.__dict__ or {})
        Routes.generate(app)
        return app

APP = Server().create_app(config=DevelopmentConfig)


if __name__ == '__main__':
    APP.run()
