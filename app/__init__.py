import os
from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from .models import db
from .auth import auth_bp
from .routes import task_bp

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "sqlite:///tasks.db"
    )
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "default-dev-key")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    JWTManager(app)

    @app.route("/health")
    def health_check():
        return {"status": "up"}

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(task_bp, url_prefix="/api/tasks")

    with app.app_context():
        db.create_all()

    return app
