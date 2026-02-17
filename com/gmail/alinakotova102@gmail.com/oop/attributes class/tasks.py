class Note:

    def __init__(self, text, tags):
        self.text = text
        self.tags = tags


# ================================================================


class GameConfig:
    MAX_LEVEL = 100
    SERVER_NAME = "Stepik-RPG"


# ================================================================


class Character:
    character_count = 0

    def __init__(self, name):
        self.name = name
        Character.character_count += 1


ch_1 = Character("Alina")
ch_2 = Character("Vlad")
print(Character.character_count)

# ================================================================


class Employee:
    company = "Stepik"

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} работает в компании {Employee.company} на должности {self.position}."


# ================================================================


class Config:
    theme = "light"

    def __init__(self, app_name):
        self.app_name = app_name

    def get_theme(self):
        return self.theme
