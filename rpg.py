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

# Выбор 1 героя
name = int(input('Выбирите героя (номер по порядку)'))
match name:
    case 1: first_knight.assignment(knight)
    case 2: first_knight.assignment(ninja)
    case 3: first_knight.assignment(archer)
    case 4: first_knight.assignment(heavy_knight)
    case 5: first_knight.assignment(student)

# Выбор 1 оружия
weapon = int(input('Выбирите оружие (номер по порядку)'))
match weapon:
    case 1: first_weapon.assignment(sword)
    case 2: first_weapon.assignment(rapier)
    case 3: first_weapon.assignment(bow)
    case 4: first_weapon.assignment(claymore)
    case 5: first_weapon.assignment(axe)

# Выбор 2 героя
name = int(input('Выбирите второго героя (обязательно другой герой)'))
match name:
    case 1: second_knight.assignment(knight)
    case 2: second_knight.assignment(ninja)
    case 3: second_knight.assignment(archer)
    case 4: second_knight.assignment(heavy_knight)
    case 5: second_knight.assignment(student)

# Выбор 2 оружия
weapon = int(input('Выбирите оружие (обязательно другое оружие)'))
match weapon:
    case 1: first_weapon.assignment(sword)
    case 2: first_weapon.assignment(rapier)
    case 3: first_weapon.assignment(bow)
    case 4: first_weapon.assignment(claymore)
    case 5: first_weapon.assignment(axe)

print('')

# Коррекция статов героев
first_knight.stats(first_weapon)
second_knight.stats(second_weapon)

# Вывожу инфу о героях и их оружиях на экран
first_knight.print_info(first_weapon)
second_knight.print_info(second_weapon)

# Бой
first_knight.fight(second_knight)
# Баланс. Нужен баланс
