from core import Human
from characters import Warrior, Mage, Healer
from battle import Battle

warrior = Warrior("Свен", lvl=10, hp=80, mp=30, power=22, lovk=9, intell=7)
mage = Mage("Фантом Лансер", lvl=10, hp=70, mp=100, power=16, lovk=14, intell=22)
healer = Healer("Вич Доктор", lvl=10, hp=60, mp=80, power=9, lovk=11, intell=18)

heroes = [warrior, mage, healer]

boss = Human("Рошан", lvl=15, hp=300, mp=150, power=35, lovk=18, intell=12)

battle = Battle(heroes, boss)
battle.start_battle()