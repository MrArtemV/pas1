from weapon import Weapon
from hero import Hero

# Задаю свойства оружию и героям
rapier = Weapon('Рапира "Ярость Бездны" ', 3, 450, 2.7, 70, 65)
claymore = Weapon('Меч безжалостной волны', 14, 1900, 0.8, 175, 50)
axe = Weapon('Топор раскола', 9, 2300, 0.9, 500, 10)
bow = Weapon('Лук растущей бури', 4, 600, 2.9, 0, 0)
sword = Weapon('Рубитель времени', 5, 1600, 1.1, 125, 50)

f_knight = Hero('Гер Какёин', '90', 17500, 500, 1500, rapier)
s_knight = Hero('Альфред Фон Дио', '87', 17500, 500, 1500, sword)

# Вывожу инфу о героях и их оружиях на экран
f_knight.print_info(rapier)
s_knight.print_info(claymore)

# Бой
f_knight.fight(s_knight)
