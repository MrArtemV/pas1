import random


class Hero:
    def __init__(self, weapon, name, hp, armor, attack):
        self.__name = name
        self.hp = hp
        self.__armor = armor
        self.__attack = attack + weapon.attack

    def __str__(self):
        return f"Статы героя \"{self.__name}\"\nздоровье: {self.hp}\tатака: {self.__attack}\nзащита: {self.__armor}\n"

    @property
    def name(self):
        return self.__name

    @property
    def armor(self):
        return self.__armor

    @property
    def attack(self):
        return self.__attack

    def fight(self, opponent):
        print(f"{self.__name} решил сразиться с героем {opponent.name}!")
        first = random.randint(0, 1)
        if first == 1:
            print(f"Первым аттакует {self.name}:\n")
            while True:
                if opponent.hp <= 0:
                    print(f"{opponent.name} мёртв!")
                    break
                self.shot(self, opponent)
                self.shot(opponent, self)

        else:
            print(f"Первым аттакует {opponent.name}:\n")
            while True:
                self.shot(opponent, self)
                if self.hp <= 0:
                    print(f"{self.name} мёртв!")
                    break
                self.shot(self, opponent)

    def shot(self, master, slave):
        slave.hp = slave.hp - (master.attack - slave.armor)
        if slave.hp <= 0:
            slave.hp = 0
        print(f"здоровье {slave.name} опустилось до {slave.hp}: атаковал {master.name}")
        input("Что бы продолжить, нажмите любую кнопку.\n")
