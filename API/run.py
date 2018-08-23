"""
runs the application
"""
from flask import Flask
from .config import DevelopmentConfig
from .app.modal import Datastore
from .app.views import Routes


class Server:
    """Create flask object to start the server"""

    @staticmethod
    def create_app(config=None):
        """performs configurations"""
        app = Flask(__name__)
        app.config.update(config.__dict__ or {})
        Routes.generate_routes(app)
        return app

apps = Server().create_app(config=DevelopmentConfig)


if __name__ == '__main__':
    apps.run()
