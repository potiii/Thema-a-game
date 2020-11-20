import os
import sys
from random import randint


class Battle:
    def __init__(self):
        # 数値の調整
        self.prince_hp = 24
        self.stinker_hp = 22
        self.stinker_super_hp = 30

        self.prince_atk_ratio = 6
        self.sword_atk_ratio = 3
        self.stinker_atk_ratio = 12
        self.stinker_super_atk_ratio = 13

    def test_fight(self):
        while True:
            os.system('cls')
            print("1) Fight Stinker without sword")
            print("2) Fight Stinker with sword")
            print("3) Fight Super Stinker without sword")
            print("4) Fight Super Stinker with sword")
            print("5) Stop test session")
            select = input("Please enter your selection: ")
            while True:
                if select == '1':
                    self.battle_loop(equip_sword=False, is_super=False)  # 武器なし,敵弱い
                    break
                elif select == '2':
                    self.battle_loop(equip_sword=True, is_super=False)  # 武器あり,敵弱い
                    break
                elif select == '3':
                    self.battle_loop(equip_sword=False, is_super=True)  # 武器なし,敵強い
                    break
                elif select == '4':
                    self.battle_loop(equip_sword=True, is_super=True)  # 武器あり,敵強い
                    break
                elif select == '5':
                    sys.exit()
                else:
                    break

    def battle(self, equip_sword, is_super):
        prince_hp = self.prince_hp
        stinker_hp = self.stinker_hp

        while True:
            stinker_hp -= self.prince_attack(equip_sword)
            if stinker_hp <= 0:
                return True
            prince_hp -= self.stinker_attack(is_super)
            if prince_hp <= 0:
                return False

    def battle_loop(self, equip_sword=False, is_super=False):  # 武器のありなし,敵の強さをT/Fで管理
        os.system('cls')
        num = 10000  # 試行回数
        win = 0
        lose = 0
        for _ in range(num):
            temp = self.battle(equip_sword, is_super)
            if temp:
                win += 1
            else:
                lose += 1

        win_rate = win / num * 100
        lose_rate = lose / num * 100

        print('win:', win)
        print('win_rate:', win_rate)
        print('lose:', lose)
        print('lose_rate:', lose_rate)

        return

    def prince_attack(self, equip_sword):
        damage = randint(1, 10000) % self.prince_atk_ratio
        if equip_sword:
            damage *= self.sword_atk_ratio
        return damage

    def stinker_attack(self, is_super):
        if not is_super:
            damage = randint(1, 10000) % self.stinker_atk_ratio
        else:
            damage = randint(1, 10000) % self.stinker_super_atk_ratio

        return damage


def main():
    battle = Battle()
    battle.test_fight()


if __name__ == '__main__':
    main()
