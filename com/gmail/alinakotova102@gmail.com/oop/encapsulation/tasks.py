# Создание защищенного атрибута
class BankAccount:
    def __init__(self, balance):
        self._balance = balance


# ================================================================


class LightSwitch:
    def __init__(self):
        self._is_on = False

    def toggle(self):
        self._is_on = not self._is_on

    def is_on(self):
        return self._is_on


# ================================================================


class Secret:
    def __init__(self, secret_message):
        self._message = secret_message

    def get_message(self):
        return self._message


# ================================================================


class User:
    def __init__(self):
        self._age = 0

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age >= 0:
            self._age = new_age


user = User()
print(user.get_age())
user.set_age("sddd")
print(user.get_age())

# ================================================================


class Thermostat:
    def __init__(self, temp):
        self._temperature = temp

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, new_temp):
        if isinstance(new_temp, int) and 0 <= new_temp <= 100:
            self._temperature = new_temp


th = Thermostat(200)
print(th.get_temperature())
th.set_temperature(0)
print(th.get_temperature())
th.set_temperature(100)
print(th.get_temperature())
th.set_temperature(-1)
print(th.get_temperature())
th.set_temperature(101)
print(th.get_temperature())
