from flask import Flask
from .routes import main
import os

def create_app():
    # Application factory for the Flask app.
    # Sets up template and static folder paths and registers Blueprints.
    #
    # NOTE: The template_folder and static_folder paths are set explicitly
    # because our 'templates' and 'static' directories are located one level
    # above this file (outside the 'main' package). This ensures Flask can
    # find and serve templates and static files correctly.
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
        static_folder=os.path.join(os.path.dirname(__file__), '..', 'static')
    )
    app.register_blueprint(main)
    return app