import pyrebase


class DBException(Exception): pass


class PhoneExists(DBException): pass


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

    def _get_logins(self):
        return dict(self.db.child("User_rest").get().val())

    def is_login(self, phone, password) -> True or False:
        try:
            return self._get_logins()[phone]['Password'] == password
        except KeyError:
            return False

    def is_phone_exists(self, phone) -> True or False:
        return phone in self._get_logins()

    def sign_up(self, phone, name, password) -> None:
        if self.is_phone_exists(phone):
            raise PhoneExists(phone)
        self.db.child("User_rest").child(phone).set({"Name": name, "Password": password})

    def get_dishes(self, phone) -> [dict]:
        rest_id = list(dict(self.db.child("Restaurant").order_by_child("User_restId").equal_to(phone).get().val()).keys())[0]
        categories = list(self.db.child("Category").order_by_child("RestId").equal_to(rest_id).get().val().keys())
        dish_categories = []
        for category in categories:
            try:
                dish_categories += self.db.child("Food").order_by_child("MenuID").equal_to(category).get().val()
            except IndexError:
                pass

        return [dict(self.db.child("Food").child(dish_category).get().val()) for dish_category in dish_categories]

    def add_dish(self, phone, info) -> None:
        pass

    def add_category(self, phone, name, image) -> None:
        pass


config = {
        "apiKey": "AIzaSyCnFkq69GKFykAjmv3_uaWIM-0KSh6wfRA",
        "authDomain": "mobile-waiter-4ed9f.firebaseapp.com",
        "databaseURL": "https://mobile-waiter-4ed9f.firebaseio.com/",
        "storageBucket": "mobile-waiter-4ed9f.appspot.com"
    }

CONNECTION = Connection(config)


if __name__ == '__main__':
    print(CONNECTION.is_login("6666", "123"))
    print(CONNECTION.is_phone_exists("7777"))
    # CONNECTION.sign_up("2722", "Andrey", "Lox")
    for dish in CONNECTION.get_dishes("6666"):
        print(dish)
