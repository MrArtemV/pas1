from weapon import Weapon
from hero import Hero

knife = Weapon("Ножи Дио", 100)
dio = Hero(knife, "Дио Брандо", 2000, 10, 30)
jotaro = Hero(knife, "Джотаро", 2000, 20, 30)

print(knife)
print(dio)
print(jotaro)

jotaro.fight(dio)
