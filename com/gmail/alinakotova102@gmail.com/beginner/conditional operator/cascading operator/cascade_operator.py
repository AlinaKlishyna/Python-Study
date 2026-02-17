# В этом примере уровень вложенности настолько глубок, что код становится трудно понять
grade = int(input("Введите вашу отметку по 100-балльной системе: "))

if grade >= 90:
    print(5)
else:
    if grade >= 80:
        print(4)
    else:
        if grade >= 70:
            print(3)
        else:
            if grade >= 60:
                print(2)
            else:
                print(1)


# Каскадный условный оператор
# Если требуется проверить несколько условий, в языке Python используется каскадный условный оператор.

# Синтаксис каскадного условного оператора имеет следующий вид:

# if условие1:
#    блок кода
# elif условие2:
#    блок кода
# ...
# else:
#    блок кода

grade = int(input("Введите вашу отметку: "))

if grade >= 90:
    print(5)
elif grade >= 80:
    print(4)
elif grade >= 70:
    print(3)
elif grade >= 60:
    print(2)
else:
    print(1)

#!! Запомни. Заключительный блок else в операторе if-elif-else является необязательным
traffic_light_signal = input("Введите сигнал светофора: ")

if traffic_light_signal == "красный":
    print("Стой!")
elif traffic_light_signal == "желтый":
    print("Приготовься...")
elif traffic_light_signal == "зеленый":
    print("Иди!")
