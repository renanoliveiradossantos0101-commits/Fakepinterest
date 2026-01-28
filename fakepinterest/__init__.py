from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os
import cloudinary
import cloudinary.uploader


local = False
if local == False:
    caminho = os.getenv("DATABASE_URL")
else:
    caminho = "sqlite:///comunidade.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = caminho
app.config["SECRET_KEY"] = "cbb76c358d4ede83459dd3f885154329"
# app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

from fakepinterest import routes