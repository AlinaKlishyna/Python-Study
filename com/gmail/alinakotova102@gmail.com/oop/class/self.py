# Знакомство с self


class Player:
    pass


# Создаем "пустые" объекты
warrior = Player()
mage = Player()

# Вручную дадим им атрибуты (пока без __init__)
warrior.name = "Конан"
warrior.health = 100

mage.name = "Гэндальф"
mage.health = 70


# Вот что происходит за кулисами. Когда вы пишете код:
warrior.take_damage(20)

# !! Python видит это и автоматически, неявно для вас, преобразует этот вызов в следующий вид:
Player.take_damage(warrior, 20)


# Именно поэтому в определении метода мы обязаны предусмотреть место для этого аргумента
# И по всеобщему соглашению программистов на Python, этот первый параметр, который принимает сам объект, всегда называется self

# !! self — это просто имя переменной, в которую метод получает ссылку на тот экземпляр объекта, для которого он был вызван

# ================================================================


# Полный пример в коде
class Player:
    # Метод для отображения информации
    def show_info(self):
        # 'self' здесь - это ссылка на конкретного игрока (warrior или mage)
        print(f"Игрок: {self.name}, Здоровье: {self.health}")

    # Метод для получения урона
    def take_damage(self, amount):
        print(f"Игрок {self.name} получает {amount} ед. урона!")

        # Мы меняем атрибут именно того игрока, который вызвал метод
        self.health = self.health - amount

        print(f"Оставшееся здоровье: {self.health}")


# 1. Подготовка
warrior = Player()
warrior.name = "Конан"
warrior.health = 100

mage = Player()
mage.name = "Гэндальф"
mage.health = 70

# 2. Проверяем исходное состояние
warrior.show_info()
mage.show_info()

print("--- Битва начинается! ---")

# 3. Атакуем ТОЛЬКО воина
# В этот момент Python передает 'warrior' в метод как 'self'
warrior.take_damage(15)

print("---")

# 4. Проверяем состояние обоих после атаки
warrior.show_info()
mage.show_info()
