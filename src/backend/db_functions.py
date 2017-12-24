import pyrebase


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

    def is_login(self, phone, password) -> True or False:
        pass

    def is_phone_exists(self, phone) -> True or False:
        pass

    def sign_up(self, phone, name, password) -> None:
        pass

    def get_dishes(self, phone) -> [dict]:
        pass

    def add_dish(self, phone, info) -> None:
        pass

    def add_category(self, phone, name) -> None:
        pass


config = {
        "apiKey": "AIzaSyCnFkq69GKFykAjmv3_uaWIM-0KSh6wfRA",
        "authDomain": "mobile-waiter-4ed9f.firebaseapp.com",
        "databaseURL": "https://mobile-waiter-4ed9f.firebaseio.com/",
        "storageBucket": "mobile-waiter-4ed9f.appspot.com"
    }

CONNECTION = Connection(config)



