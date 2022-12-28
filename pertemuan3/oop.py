class Hero:
    name = "Alucard"
    hp = 300
    damage = 200
    defense = 100

    def init (name, hp, damage, defense):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defense = defense

    def attack(self, target):
        target.hp = target.hp - self.damage 
        print("Sisa HP ", target.name, "=", target.hp)

# inisialisasi class hero
hero1 = Hero("Hayabusa", 200, 300, 15)
hero2 = Hero ("Atlas", 3000, 50, 300)

hero1.attack(hero1)
hero2.attack(hero2)