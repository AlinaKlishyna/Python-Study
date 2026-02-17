# __init__ вызывается АВТОМАТИЧЕСКИ


class Player:
    def __init__(self, name, health):
        # Этот код выполнится АВТОМАТИЧЕСКИ в момент создания объекта
        print(f"Создается новый игрок с именем {name}!")

        # Мы берем переданные значения (name, health)
        # и сохраняем их как АТРИБУТЫ объекта (через self)
        self.name = name
        self.health = health
        print(f"Игрок {self.name} успешно создан с {self.health} HP.")

    def show_info(self):
        print(f"Игрок: {self.name}, Здоровье: {self.health}")


# --- А теперь создаем игроков НОВЫМ, правильным способом ---

# Эта одна строка теперь делает ВСЁ: создает объект и настраивает его
warrior = Player("Конан", 100)

mage = Player("Гэндальф", 70)

print("--- Игроки в сборе! ---")
warrior.show_info()
mage.show_info()
print()

# ================================================================


# Создаем уникальные объекты
class Book:
    def __init__(self, title, author, year):
        # Получаем аргументы и сохраняем их как атрибуты
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True  # Атрибут по умолчанию

    def show_info(self):
        status = "в наличии" if self.is_available else "выдана"
        print(f'"{self.title}", {self.author} ({self.year} г.) - Статус: {status}')


# Создаем первый объект-книгу
book_1 = Book("Хоббит, или Туда и обратно", "Дж. Р. Р. Толкин", 1937)

# Создаем второй, совершенно другой объект
book_2 = Book("1984", "Джордж Оруэлл", 1949)

book_1.show_info()
book_2.show_info()
print()

# ================================================================


class Player:
    def __init__(self, name, health):
        # До выполнения этих строк у объекта, на который указывает self,
        # еще нет атрибутов .name и .health

        # Шаг 1: Берем значение из параметра 'name' ("Конан")
        # и создаем внутри объекта 'self' атрибут 'name' с этим значением.
        self.name = name

        # Шаг 2: Берем значение из параметра 'health' (100)
        # и создаем внутри объекта 'self' атрибут 'health' с этим значением.
        self.health = health


# Вызов:
warrior = Player("Конан", 100)
print()

# ================================================================


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} лает: Гав-гав!"


dog = Dog("Sharik")
print(dog.bark())
print()

# ================================================================


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity


product = Product("Table", 104.45, 2)
print(product.get_total_price())
print()

# ================================================================


class Student:
    def __init__(self, name, faculty):
        # Создаем атрибуты экземпляра.
        # Они будут уникальны для каждого студента.
        self.name = name
        self.faculty = faculty
        # Мы можем создавать атрибуты экземпляра и без параметров,
        # задавая им начальное значение по умолчанию.
        self.gpa = 0.0  # gpa - Grade Point Average (средний балл)

    def show_info(self):
        print(
            f"Студент: {self.name}, Факультет: {self.faculty}, Средний балл: {self.gpa}"
        )

    def set_gpa(self, new_gpa):
        # Этот метод изменяет атрибут экземпляра
        self.gpa = new_gpa


# Создаем ДВА разных, независимых объекта
student_ivan = Student("Иван Петров", "Физический")
student_maria = Student("Мария Сидорова", "Химический")

# Проверяем их начальное состояние
student_ivan.show_info()
student_maria.show_info()
# Вывод:
# Студент: Иван Петров, Факультет: Физический, Средний балл: 0.0
# Студент: Мария Сидорова, Факультет: Химический, Средний балл: 0.0

print("\n--- Иван сдал сессию ---")

# Изменяем состояние ТОЛЬКО у объекта student_ivan
student_ivan.set_gpa(4.7)

# Проверяем состояние обоих студентов еще раз
student_ivan.show_info()
student_maria.show_info()
# Вывод:
# Студент: Иван Петров, Факультет: Физический, Средний балл: 4.7  <-- Изменилось!
# Студент: Мария Сидорова, Факультет: Химический, Средний балл: 0.0 <-- Осталось прежним!
print()
