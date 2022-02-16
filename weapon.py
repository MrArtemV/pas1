# Создал класс оружия. Можно было бы приписать свойства оружия к классу героев, но это надо, чтобы позже создавать
# множество видов оружия
class Weapon:
    # шабллон оружия
    def __init__(self, w_name, w_weight, atk, atk_speed, crit, crit_rate):
        self.w_name = w_name
        self.w_weight = w_weight
        self.atk = atk
        self.atk_speed = atk_speed
        self.crit = crit
        self.crit_rate = crit_rate

# Создал класс героев
