class Weapon:
    def __init__(self, name, attack):
        self.__name = name
        self.__attack = attack

    def __str__(self):
        return f"{self.__name}: {self.__attack} за удар\n"

    @property
    def name(self):
        return self.__name

    @property
    def attack(self):
        return self.__attack
