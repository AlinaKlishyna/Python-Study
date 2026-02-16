# Возвращение булевых значений
# Python позволяет писать булевы функции, возвращающие либо истину (True), либо ложь (False)
# Булеву функцию можно применять для проверки условия, тогда значения True и False будут сигнализировать о его выполнении

# Булевы функции широко применяются для упрощения сложных условий, проверяемых в структурах принятия решения и структурах с повторением
number = int(input())
if number % 2 == 0:
    print("Это число чётное.")
else:
    print("Это число нечётное.")


# Этот фрагмент кода будет легче понять, если написать булеву функцию is_even(),
# которая принимает число в качестве аргумента и возвращает True, если оно чётное, или False в противном случае


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# Теперь можно переписать инструкцию if-else основной программы так, чтобы она для определения чётности переменной number вызывала функцию is_even():

number = int(input())
if is_even(number):
    print("Это число чётное.")
else:
    print("Это число нечётное.")


def is_educational_domain(url):
    return url.endswith(".edu")


urls = [
    "https://www.coursera.org",
    "https://mipt.ru",
    "https://www.edu.ru",
    "https://stepik.org",
    "https://openedu.ru",
    "https://www.mit.edu",
    "https://www.ecu.edu",
    "https://pygen.ru",
]
cnt = 0
for url in urls:
    if is_educational_domain(url):
        cnt += 1

print(cnt)
