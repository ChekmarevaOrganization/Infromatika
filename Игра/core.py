class Human:
    def __init__(self, name, lvl=1, hp=100, mp=50, power=10, lovk=10, intell=10):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.mp = mp
        self.power = power
        self.lovk = lovk
        self.intell = intell

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} получил {damage} урона. Осталось HP: {self.hp}")

    def attack(self, target):
        damage = self.power
        print(f"{self.name} атакует {target.name}!")
        target.take_damage(damage)

    def is_alive(self):
        return self.hp > 0