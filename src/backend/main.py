from flask import *

app = Flask(__name__, static_url_path='')


FOOD_INFO = "Название Описание Цена Картинка".split()


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form
        if "Sign In" in form:
            print(form["email"])
            if True:
                return redirect(url_for("account"))
        elif "Sign Up" in form:
            print(form["email"], form["phone"])
            if True:
                return redirect(url_for("account"))
    return render_template('index.html')


@app.route("/account/", methods=['GET', 'POST'])
def account():
    if request.method == "POST":
        print(*request.form.items())
    client = {
        'name': 'kek',
        'tel': 'kek',
        'address': 'kek',
        'description': 'kek',
    }
    items = {
        'shava': {
            'Название': 'kek',
            'Описание': 'kek',
            'Цена': 'kek',
            'Картинка': 'kek',
        },
        'morsik': {
            'Название': 'kek',
            'Описание': 'kek',
            'Цена': 'kek',
            'Картинка': 'kek',
        }
    }
    return render_template('account.html', client=client, info=FOOD_INFO, items=items)



# # Запрос на header от index.html
# @app.route('/views/<path:file>')
# def send_header(file):
#     return send_from_directory('templates/views', file)
#
#
# # Запрос на header от account.html
# @app.route('/account/views/<path:file>')
# def send_header_acc(file):
#     return send_from_directory('templates/views', file)
