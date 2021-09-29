from flask import Flask
from flask_migrate import Migrate, migrate
from flask_sqlalchemy import SQLAlchemy

import config

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
