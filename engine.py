from map import Map
from room import Room
from character import Prince, Stinker


class Engine:
    def __init__(self):
        # princeの現在位置を管理,初期位置は現段階では(0,0)のため初期化
        self.prince_dim_x = 0
        self.prince_dim_y = 0

    def dim_judge(self, param, dim=None):
        # param: 0 = 座標判定
        # param: 1 = 加算
        # param: 2 = 減算

        if not (dim is None and param == 0):
            return ValueError

        if param == 0:
            if ((self.prince_dim_x > 0) or (self.prince_dim_x < 5)) and (
                    (self.prince_dim_y > 0) or (self.prince_dim_y < 5)):
                return True
            else:
                return False

        elif param == 1:
            if dim + 1 < 5:
                return True
            else:
                return False
        elif param == 2:
            if dim - 1 > 0:
                return True
            else:
                return False
        else:
            return ValueError


def control_player(self):
    while True:
        player_input = input('input...:')
        if player_input == ('W' or 'w'):
            if Engine.dim_judge(0):
                if Engine.dim_judge(2, self.prince_dim_y):
                    self.prince_dim_y -= 1
                else:
                    print('Fuck You!!!!!!!!!!!')
                    continue
            else:
                print('Fuck You!!!!!!!!!!!')
                continue

        elif player_input == ('A' or 'a'):
            if Engine.dim_judge(0):
                if Engine.dim_judge(2, self.prince_dim_x):
                    self.prince_dim_x -= 1
                else:
                    print('Fuck You!!!!!!!!!!!')
                    continue
            else:
                print('Fuck You!!!!!!!!!!!')
                continue

        elif player_input == ('S' or 's'):
            if Engine.dim_judge(0):
                if Engine.dim_judge(1, self.prince_dim_y):
                    self.prince_dim_y += 1
                else:
                    print('Fuck You!!!!!!!!!!!')
                    continue
            else:
                print('Fuck You!!!!!!!!!!!')
                continue

        elif player_input == ('D' or 'd'):
            if Engine.dim_judge(0):
                if Engine.dim_judge(1, self.prince_dim_x):
                    self.prince_dim_x += 1
                else:
                    print('Fuck You!!!!!!!!!!!')
                    continue
            else:
                print('Fuck You!!!!!!!!!!!')
                continue

        else:
            print('Fuck You!!!!!!!!!!!')
            continue

