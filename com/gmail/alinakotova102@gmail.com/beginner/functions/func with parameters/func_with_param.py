# Функции с параметрами объявляются так же как функции без параметров, только с указанием в скобках

# def название_функции(параметры):
#    блок кода


def draw_box(height, width):  # функция принимает два параметра
    for i in range(height):
        print("*" * width)


draw_box(3, 3)
print()
draw_box(5, 5)
print()
draw_box(4, 10)


def print_text(txt, n):
    print(txt * n)


print_text("Hello", 5)
print_text("A", 10)


def print_hello(name):
    print(f"Hello, {name}!")


print_hello("Alina")
