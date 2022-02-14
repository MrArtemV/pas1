from random import randint


class Weapon():
    def __init__(self, w_name, w_weight, atk, atk_speed, crit, crit_rate):
        self.w_name = w_name
        self.w_weight = w_weight
        self.atk = atk
        self.atk_speed = atk_speed
        self.crit = crit
        self.crit_rate = crit_rate


class Hero():

    def __init__(self, name, lvl, health, armor, power, weap):
        self.name = name
        self.lvl = lvl
        self.health = health
        self.armor = armor
        self.power = power
        self.weight = 50
        self.apower = self.power + weap.atk
        self.speed = (1 - ((self.armor / 10 + weap.w_weight) / 100)) * weap.atk_speed
        self.crit_rate = weap.crit_rate
        self.crit = weap.crit

    def print_info(self, weap):
        print('Овации для сегодняшнего героя', self.name, self.lvl + '-го уровня')
        print('Оружие:', weap.w_name)
        print('Уровень здоровья:', self.health)
        print('Сила героя:', self.apower)
        print('С уровнем защищенности', self.armor, )
        print('Коэффицент ловкости:', self.speed, '\n')
        print('Характеристики оружия', weap.w_name, '\nБазовый урон', weap.atk, '\nСкорость атаки', weap.atk_speed,
              '\nКритической урон', weap.crit, '%', '\nШанс критического удара', weap.crit_rate, '%\n\n')

    def attack(self, knight):
        print('Нанесен удар! Герой', self.name, 'атаковал', knight.name, 'с силой удара', self.apower, '\n')

        ch = randint(1, 100)
        if ch > self.crit_rate:
            knight.health -= self.apower - knight.armor
            print('Герой', knight.name, 'принял удар!\nУдар оставил рыцарю', knight.health, 'здоровья!\n')
        else:
            damage = (self.apower - knight.armor) * 1.5 * self.crit / 100
            knight.health -= damage
            print(self.name, 'Наносит критический урон и нанес рыцарю', damage, 'урона!\nУдар оставил рыцарю',
                  knight.health, 'здоровья!\n')

        a = input('Напишите что-нибудь, чтобы продолжить.')

    def parry(self, knight):
        print('Рыцарь', knight.name, 'парировал атаку ' + self.name + '!')
        a = input('Напишите что-нибудь, чтобы продолжить.')

    def fight(self, knight):
        while self.health > 0 and knight.health > 0:
            punch_chance = self.speed
            while punch_chance > 0:
                if punch_chance > 1:
                    self.attack(knight)
                    punch_chance -= 1
                else:
                    chance = randint(1, 100)
                    if chance < punch_chance * 100:
                        self.attack(knight)
                    else:
                        self.parry(knight)
                    punch_chance = 0
                if knight.health <= 0:
                    print(knight.name, 'повержен! Овации рыцарю', self.name)
                    break
            if knight.health <= 0:
                break

            punch_chance = knight.speed
            while punch_chance > 0:
                if punch_chance > 1:
                    knight.attack(self)
                    punch_chance -= 1
                else:
                    chance = randint(1, 100)
                    if chance < punch_chance * 100:
                        knight.attack(self)
                    else:
                        knight.parry(self)
                    punch_chance = 0
                if self.health <= 0:
                    print(self.name, 'повержен! Овации рыцарю', knight.name)
                    break
            if self.health <= 0:
                break


rapier = Weapon('Рапира "Ярость Бездны" ', 3, 600, 2.7, 70, 65)
claymore = Weapon('Меч безжалостной волны', 16, 1500, 0.7, 150, 45)
f_knight = Hero('Гер Какёин', '90', 17000, 250, 1400, rapier)
s_knight = Hero('Альфред Фон Дио', '87', 19000, 400, 1600, claymore)
f_knight.print_info(rapier)
s_knight.print_info(claymore)
f_knight.fight(s_knight)