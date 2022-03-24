from random import randint


# Создал класс героев
class Hero:
    # Шаблон класса
    def __init__(self, name='', health=0, armor=0, atk=0, weight=0, agility=0, crit_rate=0):
        self.name = name
        self.health = health
        self.armor = armor
        self.atk = atk
        self.weight = weight
        self.agility = agility
        self.crit_rate = crit_rate
        self.crit = 0

    # Передача хар-к класса к герою
    def assignment(self, class_of_hero):
        self.name = class_of_hero.name
        self.health = class_of_hero.health
        self.armor = class_of_hero.armor
        self.atk = class_of_hero.atk
        self.weight = class_of_hero.weight
        self.agility = class_of_hero.agility
        self.crit_rate = class_of_hero.crit_rate

    # Финальная корректировка хар-к
    def stats(self, weapon):
        self.health += 15000
        self.armor += 500
        self.atk += 1500
        self.weight += 50
        self.weight = self.weight + weapon.ws['weight']
        self.atk = self.atk + weapon.ws['atk']
        self.agility = self.agility + ((1 - ((self.armor / 30 + self.weight / 5) / 100)) * weapon.ws['atk_speed'])
        self.crit_rate = self.crit_rate + weapon.ws['crit_rate']
        self.crit = weapon.ws['crit']
        self.hs = {'name': self.name, 'health': self.health, 'armor': self.armor, 'all_atk': self.atk,
                   'all_weight': self.weight, 'all_agility': self.agility, 'crit': self.crit,
                   'crit_rate': self.crit_rate}

    # Информация о классе
    def class_info(self):
        print('Имя героя:', self.name,
              '\nБонусные характеристики:',
              '\nЗдоровье:', self.health, '    Сила атаки:',  self.atk,
              '\nБроня:', self.armor, '    Вес:', self.weight,
              '\nЛовкость:', self.agility, '    Крит. шанс:', self.crit_rate, '\n\n')

    # Информация о готовом герое с оружием
    def print_info(self, weapon):
        # Инфа о созданном герое
        print('Овации для сегодняшнего героя', self.hs['name'], str(randint(80, 90)) + '-го уровня',
              '\nУровень здоровья:', self.hs['health'],
              '\nС уровнем защищенности', self.hs['armor'],
              '\nСила героя:', self.hs['all_atk'],
              '\nМасса героя:', self.hs['all_weight'],
              '\nКоэффицент ловкости:', self.hs['all_agility'],
              '\nХарактеристики оружия', weapon.ws['name'],
              '\nМасса:', weapon.ws['weight'],
              '\nБазовый урон:', weapon.ws['atk'],
              '\nСкорость атаки:', weapon.ws['atk_speed'],
              '\nКритической урон:', weapon.ws['crit'], '%',
              '\nШанс критического удара:', weapon.ws['crit_rate'], '%\n\n')

    # Функция атаки
    def attack(self, knight):
        print('Нанесен удар! Герой', self.hs['name'], 'атаковал', knight.hs['name'], 'с силой удара',
              self.hs['all_atk'], '\n')
        # Подсчет вероятности крит удара
        ch = randint(1, 100)
        if ch >= self.hs['crit_rate']:
            # Крит не прошел
            knight.hs['health'] -= self.hs['all_atk'] - knight.hs['armor']
            print('Герой', knight.hs['name'], 'принял удар!\nУдар оставил рыцарю', knight.hs['health'], 'здоровья!\n')
        else:
            # Крит прошел, подсчет крита
            damage = (self.hs['all_atk'] - knight.hs['armor']) * 1.5 * self.hs['crit'] / 100
            knight.hs['health'] -= damage
            print(self.hs['name'], 'Наносит критический урон и нанес рыцарю', damage, 'урона!\nУдар оставил рыцарю',
                  knight.hs['health'], 'здоровья!\n')
        # Просто чтобы оно не ушло сразу в конец кода
        input('Напишите что-нибудь, чтобы продолжить.\n')

    def parry(self, knight):
        # В случае непопадания в шанс удара
        print('Рыцарь', knight.hs['name'], 'парировал атаку ' + self.hs['name'] + '!\n')
        input('Напишите что-нибудь, чтобы продолжить.\n')
    # Фаза каста атака и применения. И завершение если хп кого-то < 0

    def fight(self, knight):
        # Условие с количеством хп
        while self.hs['health'] > 0 and knight.hs['health'] > 0:
            # Переменная, чтобы не менять основную переменную
            punch_chance = self.hs['all_agility']
            # Если ловкость упадет до 0, то ход переходит к другому
            # хотел здесь сделать систему с увелечением шанса удара при каждом промахе, но связи с побочной переменной
            # и удобством в ее использовании я отказался от этой идеи

            while punch_chance > 0:
                # Если ловкость >1 идет 1 удар 100%
                if punch_chance > 1:
                    self.attack(knight)
                    punch_chance -= 1
                else:
                    # Иначе будет рулетка. Если, к примеру, в ловкости 0,8 выпадет рандомное число 0,77,
                    # то пройдет еще один удар. Иначе парирование удара(ничего не произойдет)
                    chance = randint(1, 100)
                    if chance < punch_chance * 100:
                        self.attack(knight)
                    else:
                        self.parry(knight)
                    # Обнуление, чтобы закончился цикл
                    punch_chance = 0
                # Если избил насмерть, то досрочно закончится цикл. Да, если пройдет вторая атака, то ты ударишь труп
                # и что?
                if knight.hs['health'] <= 0:
                    print(knight.hs['name'], 'повержен!\nОвации рыцарю', self.hs['name'])
                    break
            # Я не уверен нужен ли этот break. Просто после него вроде как все заработало. Но если он не влияет ни на
            # что, то можешь убрать.
            if knight.hs['health'] <= 0:
                break
            # То же самое, но для второго героя. Т.е. self поменялся с knight, теперь второй бьет первого

            punch_chance = knight.hs['all_agility']
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
                if self.hs['health'] <= 0:
                    print(self.hs['name'], 'повержен!\nОвации рыцарю', knight.hs['name'])
                    break
