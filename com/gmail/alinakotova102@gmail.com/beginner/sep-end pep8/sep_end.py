# необязательный параметр sep команды print() позволяет установить строку, с помощью которой будут разделены аргументы (если их несколько) при печати
print("a", "b", "c")  # a b c

# параметр sep (separator – разделитель)
# По умолчанию этот параметр равен символу пробела " "
print("a", "b", "c", sep="-")  # a-b-c


# параметр end определяет строку, которая будет добавлена после вывода всех аргументов команды print()

# строки кода являются эквивалентными
print("A great man doesn't seek to lead.")
print("He's called to it. And he answers.", end="\n")

print("A great man doesn't seek to lead.", end="")
print(" He's called to it. And he answers.", end=".")

print("a", "\n", "b", "\n", "c", sep="*", end="#")

# Для разных команд print() можно задавать разные параметры sep и end
arg1 = "Hi"
sep1 = "_-_-_-_"
end1 = "#"

print()
print(arg1, "everyone", sep=sep1, end="!")
print()
print("How", "are", "u", "in", "2026?", sep=" ", end=end1)

print("Python", end="\n\n\n")

# Если аргумент в команде print() только один, то параметру sep нечего разделять. В таком случае параметр sep никак не будет влиять на выводимый текст
print("Python", sep="777")  # Python

print("a", "b", "c", sep="*")
print("d", "e", "f", sep="**", end="")
print("g", "h", "i", sep="+", end="%")
print("j", "k", "l", sep="-", end="\n")
print("m", "n", "o", sep="/", end="!")
print("p", "q", "r", sep="1", end="%")
print("s", "t", "u", sep="&", end="\n")
print("v", "w", "x", sep="%")
print("y", "z", sep="/", end="!")
print()

# Множественное присваивание
name, surname = "Alina", "Klishyna"
print("Name:", name, "\nSurname:", surname)

name, surname = input(), input()
print("Name:", name, "Surname:", surname)

# Множественное присваивание удобно использовать, когда нужно обменять значения двух переменных
name1 = "Andrey"
name2 = "Sergei"
name1, name2 = name2, name1
print(name1, name2)

# для обмена значений переменных следующий вариант не сработает
name1 = "Timur"
name2 = "Gvido"

name1 = name2  # name1 = name2 полностью стирает старое значение переменной name1
name2 = name1

name = "Timur"
name = "Arthur"  # перетирает
print(name)  # Arthur
name = "Anton"
print(name)  # Anton
