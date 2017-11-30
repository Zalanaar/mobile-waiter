from _weakref import ref

import pyrebase

URL = ''
config = {
    "apiKey": "AIzaSyCnFkq69GKFykAjmv3_uaWIM-0KSh6wfRA",
    "authDomain": "mobile-waiter-4ed9f.firebaseapp.com",
    "databaseURL": "https://mobile-waiter-4ed9f.firebaseio.com/",
    "storageBucket": "mobile-waiter-4ed9f.appspot.com"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()


def add_restaurant(database, restaurant_name, permission):
    """
    Функция добавления нового ресторана в базу данных.
    В случае если ресторан с таким именем существует, будет выдано предупреждение.
    :param database: объякт базы данных
    :param restaurant_name: Имя ресторана
    :param permission: Разрещение на добавление ресторанов с одинаковыми именами (True - можно, False - запрещено)
    :return: restaurant_id
    """
    warning = None
    check_name = database.child("Restaurant").order_by_child("Name").equal_to(restaurant_name).get()
    try:
        if check_name.val():
            warning = "Ресторан с таким именем уже есть в базе. "
    except IndexError:
        warning = None

    if warning is None or permission is True:
        data = {"Name": restaurant_name}
        key = database.child("Restaurant").push(data)
        restaurant_id = key.get("name", "")
    else:
        restaurant_id = None

    return restaurant_id


def add_category(database, restaurant_id, category_name, category_image):
    """
    Функция добавления категории меню к конкретному ресторану
    :param database: объект базы данных
    :param restaurant_id: ID ресторана, к которому добавляется категория меню
    :param category_name: название категории меню
    :param category_image: ссылка на картинку (http)
    :return: сообщение с результатом операции
    """
    check_name = database.child("Category").order_by_child("Name").equal_to(category_name) \
        .order_by_child("RestId").equal_to(restaurant_id).get()
    try:
        if check_name.val():
            return "Категория меню с таким названием уже есть в базе данного ресторана."
    except IndexError:
        data = {"Image": category_image, "Name": category_name, "RestId": restaurant_id}
        database.child("Category").push(data)
    return "Категория успешно добавлена."


def add_dish(database, category_id, dish_name, dish_description, dish_image, dish_price, dish_discount):
    check_name = database.child("Food").order_by_child("Name").equal_to(dish_name) \
        .order_by_child("MenuId").equal_to(category_id).get()
    try:
        if check_name.val():
            return "Блюдо с таким названием уже есть в базе данного меню."
    except IndexError:
        data = {"Image": dish_image, "Name": dish_name, "RestId": category_id, "Description": dish_description,
                "Price": dish_price, "Discount": dish_discount}
        database.child("Food").push(data)
    return "Блюдо успешно добавлено."


def multi_update(database, data):
    """
    data = {
            "table/key": {
                "field_name": "data"},
            "table2/key2": {
                "field_name2": "data2"}}
    :param database: 
    :param data: 
    :return: 
    """
    database.update(data)


def multi_insert(database, data):
    """
    data = {
            "table/"+ref.generate_key(): {
                "field_name": "data"},
            "table2/"+ref.generate_key(): {
                "field_name2": "data2"}}
    :param database: 
    :param data: 
    :return: 
    """
    database.update(data)


def delete(database, table_name, key):
    database.child(table_name).child(key).remove()
    return "Запись удалена."


def get_dish_list_from_menu(database, restaurant_id):
    pass


def get_dish_list_from_category(database, category_id):
    pass


def get_all_restaurants(database):
    pass


def get_categories(database, restaurant_id):
    pass


def change_order_status(database, order_id):
    pass


if __name__ == "__main__":
    id = add_restaurant(db, "MA XXL", False)
    print(id)
    add_category(db, id, "Sushi", "URL")