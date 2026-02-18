class Account:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance


# ========================================================


class Device:
    def __init__(self):
        self._voltage = 0

    def set_voltage(self, new_voltage):
        self._voltage = new_voltage

    def get_voltage(self):
        return self._voltage


# ========================================================


class Mailbox:
    def __init__(self):
        self._owner = None

    def get_owner(self):
        return self._owner

    def set_owner(self, new_owner):
        if not isinstance(new_owner, str):
            return
        self._owner = new_owner


m = Mailbox()
print(m.get_owner())  # None

m.set_owner(3)
print(m.get_owner())  # None, don't setted

m.set_owner("Pum-pum")
print(m.get_owner())  # Pum-pum, setted


# ========================================================


class MusicPlayer:
    def __init__(self):
        self._volume = 10

    def get_volume(self):
        return self._volume

    def set_volume(self, new_volume):
        if 0 <= new_volume <= 100:
            self._volume = new_volume


# ========================================================


class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = 0
        self.set_age(age)

    def set_age(self, new_age):
        if 0 <= new_age <= 120:
            self._age = new_age

    def get_age(self):
        return self._age


person = Person("Alina", 150)
print(person.get_age())
