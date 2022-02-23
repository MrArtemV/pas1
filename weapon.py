# Создал класс оружия. Можно было бы приписать свойства оружия к классу героев, но это надо, чтобы позже создавать
# множество видов оружия
class Weapon:
    # Шаблон оружия
    def __init__(self, name, weight, atk, atk_speed, crit, crit_rate):
        self.name = name
        self.weight = weight
        self.atk = atk
        self.atk_speed = atk_speed
        self.crit = crit
        self.crit_rate = crit_rate
        self.ws = {'name': self.name, 'weight': self.weight, 'atk': self.atk, 'atk_speed': self.atk_speed, 'crit': self.crit, 'crit_rate': self.crit_rate}