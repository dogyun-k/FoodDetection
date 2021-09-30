import os
import sys

# Server 디렉토리 파일 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import urllib.request

import config
from flask import Flask
from flask_migrate import Migrate, migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    # app name = file name이 담김. __name__ = "yoluServer"
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprint
    from views import main_views
    app.register_blueprint(main_views.bp)

    return app


if __name__ == '__main__':
    create_app().run()
