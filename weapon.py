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
        self.ws = {'name': self.name, 'weight': self.weight, 'atk': self.atk, 'atk_speed': self.atk_speed,
                   'crit': self.crit, 'crit_rate': self.crit_rate}

    def assignment(self, class_of_weapon):
        self.ws = class_of_weapon.ws.copy()

    # Информация об оружие
    def weapon_info(self):
        print('Название оружия:', self.ws['name'],
              '\nХарактеристики:',
              '\nСила атаки:', self.ws['atk'], '    Масса:', self.ws['weight'],
              '\nСкорость атаки:', self.ws['atk_speed'], '    Критический урон:', self.ws['crit'],
              '\nКрит.шанс:', self.ws['crit_rate'], '\n\n')
