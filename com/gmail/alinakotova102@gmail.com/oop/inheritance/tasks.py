# 1 ========================================================
class Appliance:
    def __init__(self, model):
        self.model = model
        self.is_on = False

    def turn_on(self):
        self.is_on = True


class Toaster(Appliance):
    pass


# 2 ========================================================


class Publication:
    def __init__(self, title):
        self.title = title


class Book(Publication):
    def get_author(self, author_name):
        return f"Автор книги '{self.title}' - {author_name}"


# 3 ========================================================


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id


# 4 ========================================================


class Shape:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


class Polygon(Shape):
    def __init__(self, color, num_sides):
        super().__init__(color)
        self.num_sides = num_sides


class Square(Polygon):
    def __init__(self, color, side_length):
        super().__init__(color, 4)
        self.side_length = side_length


# 5 ========================================================


class Worker:
    def __init__(self, name, position):
        self._name = name
        self._position = position


class HRManager(Worker):
    def get_employee_info(self):
        return f"Имя: {self._name}, Должность: {self._position}"
