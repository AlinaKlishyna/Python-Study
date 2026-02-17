def create_book_class():
    # Напишите ваш код здесь
    # Определите класс Book и верните его
    class Book:
        pass

    return Book


# ================================================================


class Robot:
    pass

    def say_hello(self):
        return "Привет, я робот!"


# ================================================================


class TrafficLight:
    pass

    def red_signal(self):
        return "Стоп"

    def yellow_signal(self):
        return "Внимание"

    def green_signal(self):
        return "Можно ехать"


# ================================================================


class Calculator:
    pass

    def plus(self):
        return "Сложение"

    def minus(self):
        return "Вычитание"


calc = Calculator()
print(calc.plus())
print(calc.minus())
print(calc.plus())

# ================================================================


class UserProfile:
    pass

    def show_profile(self):
        return "Это профиль пользователя."

    def edit_profile(self):
        return "Редактирование профиля."


# ================================================================


class Cat:
    def __init__(self):
        self.state = "спит"

    def get_state(self):
        return self.state


cat = Cat()
print(cat.get_state())


# ================================================================


class Book:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title


book = Book("Voina i mir")
print(f"Name book: {book.get_title()}")


# ================================================================


class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

    def get_info(self):
        return f"Имя: {self.username}, Возраст: {self.age}"


user = User("Alina", 25)
print(user.get_info())
