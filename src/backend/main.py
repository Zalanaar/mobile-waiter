from flask import Flask

from models import db


app = Flask(__name__)

# SQLite база в оперативной памяти
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# Убираем warning при старте (потом разработчики сделают дефолтом)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)


@app.route("/")
def hello():
    return "Hello World!"
