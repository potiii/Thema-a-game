class Character:
    def __init__(self, hp, attack):
        self.hp = hp
        self.max_hp = hp
        self.attack = attack

    def in_damage(self, in_damage):
        self.hp -= in_damage


class Prince(Character):
    def __init__(self, hp, attack):
        super().__init__(hp, attack)
        self.is_sword = False

    def sword_equip(self):
        if self.is_sword:
            return False

        self.is_sword = True
        self.attack += 5

    def use_potion(self):
        if self.hp < self.max_hp:
            self.hp = self.max_hp
            return True
        else:
            return False

    def in_damage(self, in_damage):
        super(Prince, self).in_damage(in_damage)


class Stinker(Character):
    def __init__(self, hp, attack, is_super=False):
        super().__init__(hp, attack)
        self.is_super = is_super

        if self.is_super:
            self.hp *= 1.2
            self.attack *= 1.2

    def in_damage(self, in_damage):
        super(Stinker, self).in_damage(in_damage)
