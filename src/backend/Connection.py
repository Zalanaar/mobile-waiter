import pyrebase


class FirebaseException(Exception):
    pass


class UserExists(FirebaseException):
    pass


class Connection:

    def __init__(self, config):
        """
        Создаёт подключение к БД Firebase.
        :param config: конфигурация подключения
        """
        # У Firebase кроме database есть ещё auth и storage
        # оставим на всякий случай
        self.firebase = pyrebase.initialize_app(config)
        # Непосредственно подключение к БД
        self.db = self.firebase.database()

    def add_restaurant(self, name):
        """
        Добавляет ресторан в БД.
        :param name: название ресторана.
        :return: id ресторана.
        """
        # push() возвращает json с id, но id там почему-то помечено как "name"
        received_json = self.db.child("Restaurant").push({"Name": name})
        return received_json['name']

    def get_restaurant(self, name):
        """
        Возвращает id ресторана по его названию.
        :param name: название ресторана.
        :return: id ресторана.
        :raises IndexError: если такого ресторана нет в БД.
        """
        return list(self.db.child("Restaurant").order_by_child("Name").equal_to(name).get().val().keys())[0]

    def has_restaurant(self, name):
        """
        Ищёт, есть ли ресторан с таким названием в БД.
        :param name: название ресторана.
        :return: True если нашёл, иначе False.
        """
        try:
            self.db.child("Restaurant").order_by_child("Name").equal_to(name).get().val()
        except IndexError:
            return False
        else:
            return True

    def add_category(self, name, image, restaurant_id):
        """
        Добавляет категорию блюд к ресторану.
        :param name: название категории.
        :param image: ссылка на картинку для отображения в мобильном приложении.
        :param restaurant_id: id ресторана.
        :return: id категории.
        """
        received_json = self.db.child("Category").push({"Name": name, "Image": image, "RestId": restaurant_id})
        return received_json["name"]

    def add_food(self, name, description, image, price, category_id):
        """
        Добавляет блюдо в категорию.
        :param name: название блюда.
        :param description: описание блюда.
        :param image: ссылка на картинку для отображения в мобильном приложении.
        :param price: цена блюда.
        :param category_id: id категории.
        :return: id блюда.
        """
        received_json = self.db.child("Food").push(
            {"Name": name, "Description": description,
             "Image": image, "Price": price, "MenuID": category_id}
        )
        return received_json["name"]

    def is_login_info_correct(self, login, password):
        """
        Проверяет, корректны ли данные для входа в систему.
        :param login: логин пользователя.
        :param password: пароль пользователя.
        :return: True если корректны, иначе False.
        """
        try:
            self.db.child("User").order_by_child("Name").equal_to(login).get().val()
            self.db.child("User").order_by_child("Password").equal_to(password).get().val()
        except IndexError:
            return False
        else:
            return True

    def register_user(self, login, password):
        """
        Регистрирует пользователя в системе.
        :param login: логин пользователя.
        :param password: пароль пользователя.
        :raises UserExists: если пользователь с таким логином уже есть в системе.
        """
        try:
            self.db.child("User").order_by_child("Name").equal_to(login).get().val()
        except IndexError:
            raise UserExists(f"User {login} already exists.")
        else:
            self.db.child("User").push({"Name": login, "Password": password})


if __name__ == "__main__":
    config = {
        "apiKey": "AIzaSyCnFkq69GKFykAjmv3_uaWIM-0KSh6wfRA",
        "authDomain": "mobile-waiter-4ed9f.firebaseapp.com",
        "databaseURL": "https://mobile-waiter-4ed9f.firebaseio.com/",
        "storageBucket": "mobile-waiter-4ed9f.appspot.com"
    }

    con = Connection(config)

    restaurant_id = con.get_restaurant("Test")
    # result = con.add_category("Чебуреки", "NoURL", restaurant_id)
    result = con.add_food("Чебурек", "Вкусный сочный чебурек", "NoURL", 150, "-L-S5_9JO54-Foj71kOl")
    print(result)
