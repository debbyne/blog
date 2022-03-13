from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    # Initialize the app
    app = Flask(__name__)
    #Initialize bootstrap
    bootstrap.init_app(app)
    # Setting up config
    app.config.from_object(config_options[config_name])
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # Setting up the config
    from .requests import configure_request
    configure_request(app)
    return app