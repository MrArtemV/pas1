from weapon import Weapon
from hero import Hero

# Создание классов оружия
sword = Weapon('Рубитель времени', 5, 1600, 1.1, 125, 50)
rapier = Weapon('Рапира "Ярость Бездны" ', 3, 450, 2.7, 70, 65)
bow = Weapon('Лук растущей бури', 4, 600, 2.9, 0, 0)
claymore = Weapon('Меч безжалостной волны', 14, 1900, 0.8, 175, 50)
axe = Weapon('Топор раскола', 9, 2300, 0.9, 500, 10)
# "Нулевые" оружия, на которые выбираются оружия
first_weapon = Weapon()
second_weapon = Weapon()
# Список для перебора
weapons = {1: sword, 2: rapier, 3: bow, 4: claymore, 5: axe}

# Создание классов героев
# Характеристики "скелета" персонажа
# 15000 (хп), 500 (броня), 1500 (сила атаки), 0 (доп. масса), 0 (доп. ловкость), 0 (доп крит. шанс)
knight = Hero('Иоанн Б.', 0, 0, 0, 0, 0, 0)
ninja = Hero('Си-Фу', -4000, -400, -250, -12,  1, 0)
archer = Hero('Усолант', -2000, -155, -300, -10, 0.7, 0)
heavy_knight = Hero('Безыменный страж', 3000, 200, 300, 15, -0.5, 0)
student = Hero('"Некто РРР"', -2500, 300, 150, -8, -0.2, 15)
# Герои, на которых выбираются классы
first_knight = Hero()
second_knight = Hero()
# Список для перебора
heroes = {1: knight, 2: ninja, 3: archer, 4: heavy_knight, 5: student}

# Описание героев и оружия
print('Герои:\n')
for i in range(1, len(heroes) + 1):
    heroes[i].class_info()
print('Оружия:\n')
for i in range(1, len(weapons) + 1):
    weapons[i].weapon_info()

# Выбор 1 героя
name = int(input('Выбирите героя (номер по порядку)\n'))
for i in range(1, len(heroes) + 1):
    if i == name:
        first_knight.assignment(heroes[i])

# Выбор 1 оружия
weapon = int(input('Выбирите оружие для 1-го героя\n'))
for i in range(1, len(weapons) + 1):
    if i == weapon:
        first_weapon.assignment(weapons[i])

# Выбор 2 героя
name = int(input('Выбирите второго героя\n'))
for i in range(1, len(heroes) + 1):
    if i == name:
        second_knight.assignment(heroes[i])

# Выбор 2 оружия
weapon = int(input('Выбирите оружие для 2-го героя\n'))
for i in range(1, len(weapons) + 1):
    if i == weapon:
        second_weapon.assignment(weapons[i])

print('')

# Коррекция статов героев
first_knight.stats(first_weapon)
second_knight.stats(second_weapon)

# Вывожу инфу о героях и их оружиях на экран
first_knight.print_info(first_weapon)
second_knight.print_info(second_weapon)

# Бой
first_knight.fight(second_knight)
# Баланс. Нужен баланс.
