from flask import Flask, render_template, request, send_from_directory

from models import db


app = Flask(__name__, static_url_path='')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/account/")
def account():
    return render_template('account.html')


@app.route("/menu/add", methods=['POST'])
def add_dish():
    print(dir(request))


# Запрос на header от index.html
@app.route('/views/<path:file>')
def send_header(file):
    return send_from_directory('templates/views', file)


# Запрос на header от account.html
@app.route('/account/views/<path:file>')
def send_header_acc(file):
    return send_from_directory('templates/views', file)


if __name__ == '__main__':
    # SQLite база в оперативной памяти
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    # Убираем warning при старте (потом разработчики сделают дефолтом)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)
