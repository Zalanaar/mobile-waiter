from collections import OrderedDict

from flask import *

from db_functions import CONNECTION

app = Flask(__name__, static_url_path='')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


FOOD_INFO = "Название Описание Картинка Категория Цена Скидка".split()


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form
        if "Sign In" in form:
            print(form['phone'], form['pass'])
            if CONNECTION.is_login(form['phone'], form['pass']):
                session['phone'] = form['phone']
                return redirect(url_for("account"))
        elif "Sign Up" in form:
            if not CONNECTION.is_phone_exists(form['phone']):
                CONNECTION.sign_up(form['phone'], form['name'], form['pass'])
                session['phone'] = form['phone']
                return redirect(url_for("account"))
    return render_template('index.html')


@app.route("/account/", methods=['GET', 'POST'])
def account():
    user = session['phone']
    if request.method == "POST":
        form = request.form
        image = form['image']
        name = form['name']
        CONNECTION.add_category(user, name, image)

    else:
        try:
            items = [item for item in CONNECTION.get_dishes(session['phone'])]
            items_ordered = []
            print(items)

            for item in items:
                kek = [item['Name'], item['Description'], item['Image'], item['MenuID'], item['Price'], item['Discount'],]
                items_ordered.append(kek)

            print(items_ordered)

        except IndexError:
            items_ordered = []

    return render_template('account.html', info=FOOD_INFO, items=items_ordered)
