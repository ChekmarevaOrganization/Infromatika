import random
class Battle:
    def __init__(self, heroes, boss):
        self.heroes = heroes
        self.boss = boss

    def start_battle(self):
        print("Заход на рошпит")

        round_number = 1

        while any(h.hp > 0 for h in self.heroes) and self.boss.hp > 0:
            print(f"\nРаунд {round_number} ")

            for hero in self.heroes:
                if hero.hp > 0 and self.boss.hp > 0:
                    hero.attack(self.boss)
            if self.boss.hp > 0:
                alive_heroes = [h for h in self.heroes if h.hp > 0]
                if alive_heroes:
                    target = random.choice(alive_heroes)
                    self.boss.attack(target)

            round_number += 1

        if any(h.hp > 0 for h in self.heroes):
            print("\nАегис выбит")
        else:
            print("\nАегис не выбит")