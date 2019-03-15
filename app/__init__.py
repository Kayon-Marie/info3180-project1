from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "Su24p3r$3cr9et0key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:password123@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
