# Создал класс оружия
class Weapon:
    # Шаблон оружия
    def __init__(self, name='', weight=0, atk=0, atk_speed=0, crit=0, crit_rate=0):
        self.name = name
        self.weight = weight
        self.atk = atk
        self.atk_speed = atk_speed
        self.crit = crit
        self.crit_rate = crit_rate

    def assignment(self, class_of_weapon):
        self.name = class_of_weapon.name
        self.weight = class_of_weapon.weight
        self.atk = class_of_weapon.atk
        self.atk_speed = class_of_weapon.atk_speed
        self.crit = class_of_weapon.crit
        self.crit_rate = class_of_weapon.crit_rate
        self.ws = {'name' : self.name, 'weight' : self.weight}

    # Информация об оружие
    def weapon_info(self):
        print('Название оружия:', self.name,
              '\nХарактеристики:',
              '\nСила атаки:', self.atk, '    Масса:', self.weight,
              '\nСкорость атаки:', self.atk_speed, '    Критический урон:', self.crit,
              '\nКрит.шанс:', self.crit_rate, '\n\n')
