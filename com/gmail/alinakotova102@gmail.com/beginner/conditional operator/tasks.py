num = int(input())
if len(str(num)) == 4:
    print("YES" if num % 7 == 0 or num % 17 == 0 else "NO")
else:
    print("NO")

# ================================================================

a = int(input())
b = int(input())
c = int(input())

print("YES" if (a + b) > c and (a + c) > b and (b + c) > a else "NO")

# ================================================================

year = int(input())
print("YES" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "NO")

# ================================================================

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
print("YES" if x1 == x2 or y1 == y2 else "NO")

# ================================================================

a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(
    "YES"
    if a - 1 <= c <= a + 1
    and b - 1 <= d <= b + 1
    and (1 <= a <= 8 and 1 <= b <= 8 and 1 <= c <= 8 and 1 <= d <= 8)
    else "NO"
)

# ================================================================

num1, num2, num3 = int(input()), int(input()), int(input())

if num1 < num2 < num3 or num1 > num2 > num3:
    print(num2)
elif num2 < num3 < num1 or num2 > num3 > num1:
    print(num3)
elif num3 < num1 < num2 or num3 > num1 > num2:
    print(num1)

# ================================================================

month = int(input())

if month == 2:
    print(28)
elif month in (4, 6, 9, 11):
    print(30)
else:
    print(31)

# ================================================================


weight = int(input())

if weight < 60:
    print("Легкий вес")
elif weight < 64:
    print("Первый полусредний вес")
else:
    print("Полусредний вес")

# ================================================================

num1 = int(input())
num2 = int(input())
str = input()


if str == "+" or str == "-" or str == "*" or str == "/":
    if str == "+":
        print(num1 + num2)
    if str == "-":
        print(num1 - num2)
    if str == "*":
        print(num1 * num2)
    if str == "/":
        if num1 != 0 and num2 != 0:
            print(num1 / num2)
        elif num1 == 0 and num2 != 0:
            print(num1 / num2)
        else:
            print("На ноль делить нельзя!")
else:
    print("Неверная операция")

# ================================================================

color1 = input()
color2 = input()

red = "красный"
blue = "синий"
yellow = "желтый"
violet = "фиолетовый"
orange = "оранжевый"
green = "зеленый"

res = "ошибка цвета"
if color1 == red and color2 == red:
    res = red
if color1 == blue and color2 == blue:
    res = blue
if color1 == yellow and color2 == yellow:
    res = yellow

if color1 == red and color2 == blue or color2 == red and color1 == blue:
    res = violet
elif color1 == red and color2 == yellow or color2 == red and color1 == yellow:
    res = orange
elif color1 == blue and color2 == yellow or color2 == blue and color1 == yellow:
    res = green

print(res)

# ================================================================

num = int(input())

if num == 0:
    print("зеленый")
elif 1 <= num <= 10:
    if num % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 11 <= num <= 18:
    if num % 2 == 0:
        print("красный")
    else:
        print("черный")
elif 19 <= num <= 28:
    if num % 2 == 0:
        print("черный")
    else:
        print("красный")
elif 29 <= num <= 36:
    if num % 2 == 0:
        print("красный")
    else:
        print("черный")
else:
    print("ошибка ввода")

# ================================================================
