from weapon import Weapon
from hero import Hero

# Задаю свойства оружию и героям
rapier = Weapon('Рапира "Ярость Бездны" ', 3, 450, 2.7, 70, 65)
claymore = Weapon('Меч безжалостной волны', 16, 1600, 0.8, 170, 45)
axe = Weapon('Топор раскола', 10, 1800, 0.85, 400, 5)

f_knight = Hero('Гер Какёин', '90', 17000, 250, 1400, rapier)
s_knight = Hero('Альфред Фон Дио', '87', 19000, 400, 1600, claymore)
# Вывожу инфу о героях и их оружиях на экран
f_knight.print_info(rapier)
s_knight.print_info(claymore)
# Бой
f_knight.fight(s_knight)
# Полный дисбаланс, Какёин побеждает всегда. Если разберешься, то можешь баланснуть так, чтобы было четко
