from weapon import Weapon
from hero import Hero

# Задаю свойства оружию и героям
sword = Weapon('Рубитель времени', 5, 1600, 1.1, 125, 50)
rapier = Weapon('Рапира "Ярость Бездны" ', 3, 450, 2.7, 70, 65)
bow = Weapon('Лук растущей бури', 4, 600, 2.9, 0, 0)
claymore = Weapon('Меч безжалостной волны', 14, 1900, 0.8, 175, 50)
axe = Weapon('Топор раскола', 9, 2300, 0.9, 500, 10)
first_weapon = Weapon()
second_weapon = Weapon()

# Характеристики "скелета" персонажа
# 15000 (хп), 500 (броня), 1500 (сила атаки), 0 (доп. масса), 0 (доп. ловкость), 0 (доп крит. шанс)
knight = Hero('Иоанн Б.', 0, 0, 0, 0, 0, 0)
ninja = Hero('Си-Фу', -4000, -400, -250, -12,  1, 0)
archer = Hero('Усолант', -2000, -155, -300, -10, 0.7, 0)
heavy_knight = Hero('Безыменный страж', 3000, 200, 300, 15, -0.5, 0)
student = Hero('"Некто РРР"', -2500, 300, 150, -8, -0.2, 15)
first_knight = Hero()
second_knight = Hero()

# Описание героев и оружия
print('Герои:\n')
knight.class_info()
ninja.class_info()
archer.class_info()
heavy_knight.class_info()
student.class_info()
print('Оружия:\n')
sword.weapon_info()
rapier.weapon_info()
bow.weapon_info()
claymore.weapon_info()
axe.weapon_info()

name = int(input('Выбирите героя (номер по порядку)'))
if name == 1:
    first_knight.assignment(knight)
elif name == 2:
    first_knight.assignment(ninja)
elif name == 3:
    first_knight.assignment(archer)
elif name == 4:
    first_knight.assignment(heavy_knight)
elif name == 5:
    first_knight.assignment(student)


weapon = int(input('Выбирите оружие (номер по порядку)'))
if weapon == 1:
    first_weapon.assignment(sword)
if weapon == 2:
    first_weapon.assignment(rapier)
if weapon == 3:
    first_weapon.assignment(bow)
if weapon == 4:
    first_weapon.assignment(claymore)
if weapon == 5:
    first_weapon.assignment(axe)

s_name = int(input('Выбирите второго героя (обязательно другой герой)'))
if s_name == 1:
    second_knight.assignment(knight)
elif s_name == 2:
    second_knight.assignment(ninja)
elif s_name == 3:
    second_knight.assignment(archer)
elif s_name == 4:
    second_knight.assignment(heavy_knight)
elif s_name == 5:
    second_knight.assignment(student)

while name == s_name:
    print('Этот герой занят!')
    s_name = int(input('Выбирите второго героя'))
    if s_name == 1:
        second_knight.assignment(knight)
    elif s_name == 2:
        second_knight.assignment(ninja)
    elif s_name == 3:
        second_knight.assignment(archer)
    elif s_name == 4:
        second_knight.assignment(heavy_knight)
    elif s_name == 5:
        second_knight.assignment(student)

s_weapon = int(input('Выбирите оружие (обязательно другое оружие)'))
if s_weapon == 1:
    second_weapon.assignment(sword)
if s_weapon == 2:
    second_weapon.assignment(rapier)
if s_weapon == 3:
    second_weapon.assignment(bow)
if s_weapon == 4:
    second_weapon.assignment(claymore)
if s_weapon == 5:
    second_weapon.assignment(axe)

while weapon == s_weapon:
    print('Это оружие занято!')
    s_weapon = int(input('Выбирите оружие'))
    if s_weapon == 1:
        second_weapon.assignment(sword)
    if s_weapon == 2:
        second_weapon.assignment(rapier)
    if s_weapon == 3:
        second_weapon.assignment(bow)
    if s_weapon == 4:
        second_weapon.assignment(claymore)
    if s_weapon == 5:
        second_weapon.assignment(axe)

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
