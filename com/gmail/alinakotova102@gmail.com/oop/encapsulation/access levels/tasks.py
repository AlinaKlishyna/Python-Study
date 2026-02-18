class AppSettings:
    def __init__(self, user_id, theme):
        self.user_id = user_id  # user_id - публичный атрибут
        self._theme = theme  # _theme - защищенный атрибут


# ================================================================


class DatabaseConnector:
    def __init__(self):
        self.is_connected = False

    def _establish_connection(self):
        self.is_connected = True

    def connect(self):
        self._establish_connection()


db = DatabaseConnector()
print(db.is_connected)
db.connect()
print(db.is_connected)


# ================================================================


class APIClient:
    def __init__(self, api_key):
        self.__api_key = api_key


api_client = APIClient("TTT-900")
try:
    print(api_client.__api_key)
except AttributeError as e:
    print(f"Error: {e}")
print(
    api_client._APIClient__api_key
)  # так лучше не делать, так как мы берем приватный атрибут хитрым путем

# ================================================================


class Component:
    def __init__(self, name, version, _id):
        self.name = name  # public
        self._id = _id  # protected
        self.__version = version  # private


# ================================================================


class Worker:
    __salary = 1000  #  self.__salary - приватная переменная

    def get_salary(self):
        return self.__salary


worker = Worker()
print(worker._Worker__salary)  # получим 1000, но так плохо брать приватную переменную
# лучше через публичный метод, который ее забирает
print(worker.get_salary())

print(worker.__salary)

# ================================================================


class Worker:
    def __init__(self):
        self.__salary = 50000

    def get_info(self):
        return f"Зарплата: {self.__salary}"
