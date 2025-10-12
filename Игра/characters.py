from core import Human

class Warrior(Human):
    def attack(self, target):
        damage = self.power
        print(f"{self.name} атакует мечом {target.name}!")
        target.take_damage(damage)

class Mage(Human):
    def attack(self, target):
        damage = self.lovk
        print(f"{self.name} стреляет спирит лансом {target.name}!")
        target.take_damage(damage)

class Healer(Human):
    def attack(self, target):
        damage = self.intell
        print(f"{self.name} атакует маледиктом {target.name}!")
        target.take_damage(damage)