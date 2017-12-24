from flask import *

app = Flask(__name__, static_url_path='')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


FOOD_INFO = "Название Описание Цена Картинка Категория".split()


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = request.form
        if "Sign In" in form:
            if True:
                session['user'] = form['phone']
                return redirect(url_for("account"))
        elif "Sign Up" in form:
            print(form["email"], form["phone"])
            if True:
                return redirect(url_for("account"))
    return render_template('index.html')


@app.route("/account/", methods=['GET', 'POST'])
def account():
    user = session['user']
    if request.method == "POST":
        print(*request.form.items())
    # client = {
    #     'name': 'kek',
    #     'tel': 'kek',
    # }
    items = [['kek', 'kek', 'kek', 'kek', 'kek'],
             ['shpek', 'shpek', 'shpek', 'shpek', 'shpek']]

    return render_template('account.html', info=FOOD_INFO, items=items)
