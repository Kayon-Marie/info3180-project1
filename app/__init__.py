from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "Su24p3r$3cr9et0key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://xgnoajsclwmuib:b52ed944b47ea3d16a8d76b5af5ac5513102d2c4ef43cc13c0e7a69e5621f273@ec2-107-20-177-161.compute-1.amazonaws.com:5432/dbhjgd4v52okf4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = './app/static/uploads'

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
