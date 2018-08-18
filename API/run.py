"""
app root of the api endpoints
"""


from config import DevelopmentConfig, ProductionConfig
from flask import Flask
from app.modal import *
from app.views import *


class Server:
    """Create flask object to start the server"""

    @staticmethod
    def create_app(config=None):
        app = Flask(__name__)
        app.config.update(config.__dict__ or {})
        Routes.generate(app)
        return app


App = Server().create_app(config=DevelopmentConfig)


if __name__ == '__main__':
    App.run()
