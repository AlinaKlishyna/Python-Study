age = int(input("Сколько вам лет?: "))
grade = int(input("В каком классе вы учитесь?: "))
if age >= 12 and grade >= 7:
    print("Доступ разрешен.")
else:
    print("Доступ запрещен.")


age = int(input("Сколько вам лет?: "))
grade = int(input("В каком классе вы учитесь?: "))
city = input("В каком городе вы живете?: ")
if age >= 12 and grade >= 7 and city == "Москва":
    print("Доступ разрешен.")
else:
    print("Доступ запрещен.")


city = input("В каком городе вы живете?: ")
if city == "Москва" or city == "Санкт-Петербург" or city == "Екатеринбург":
    print("Доступ разрешен.")
else:
    print("Доступ запрещен.")


age = int(input("Сколько вам лет?: "))
grade = int(input("В каком классе вы учитесь?: "))
city = input("В каком городе вы живете?: ")
if age >= 12 and grade >= 7 and (city == "Москва" or city == "Санкт-Петербург"):
    print("Доступ разрешен.")
else:
    print("Доступ запрещен.")


age = int(input("Сколько вам лет?: "))
if not (age < 12):
    print("Доступ разрешен.")
else:
    print("Доступ запрещен.")
