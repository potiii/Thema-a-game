from fuck.Room import Room
from fuck.Character import Stinker, Prince


# stinker hp 25 attack 3 (1,4)(2,1)
# super stinker (3,3)

# prince hp 20 attack 5


class Map:
    def __init__(self, **kwargs):
        self.max_map_size_x = kwargs['max_map_size_x'] if 'max_map_size_x' in kwargs and kwargs['max_map_size_x'] else 5
        self.max_map_size_y = kwargs['max_map_size_y'] if 'max_map_size_y' in kwargs and kwargs['max_map_size_y'] else 5
        loc_sword_x = kwargs['loc_sword_x'] if 'loc_sword_x' in kwargs and kwargs['loc_sword_x'] else 0
        loc_sword_y = kwargs['loc_sword_y'] if 'loc_sword_y' in kwargs and kwargs['loc_sword_y'] else 3
        loc_potion1_x = kwargs['loc_potion1_x'] if 'loc_potion1_x' in kwargs and kwargs['loc_potion1_x'] else 2
        loc_potion1_y = kwargs['loc_potion1_y'] if 'loc_potion1_y' in kwargs and kwargs['loc_potion1_y'] else 4
        loc_potion2_x = kwargs['loc_potion2_x'] if 'loc_potion2_x' in kwargs and kwargs['loc_potion2_x'] else 4
        loc_potion2_y = kwargs['loc_potion2_y'] if 'loc_potion2_y' in kwargs and kwargs['loc_potion2_y'] else 2
        loc_prince_x = kwargs['loc_prince_x'] if 'loc_prince_x' in kwargs and kwargs['loc_prince_x'] else 0
        loc_prince_y = kwargs['loc_prince_y'] if 'loc_prince_y' in kwargs and kwargs['loc_prince_y'] else 0
        loc_stinker1_x = kwargs['loc_stinker1_x'] if 'loc_stinker1_x' in kwargs and kwargs['loc_stinker1_x'] else 1
        loc_stinker1_y = kwargs['loc_stinker1_y'] if 'loc_stinker1_y' in kwargs and kwargs['loc_stinker1_y'] else 4
        loc_stinker2_x = kwargs['loc_stinker2_x'] if 'loc_stinker2_x' in kwargs and kwargs['loc_stinker2_x'] else 2
        loc_stinker2_y = kwargs['loc_stinker2_y'] if 'loc_stinker2_y' in kwargs and kwargs['loc_stinker2_y'] else 1
        loc_super_x = kwargs['loc_super_x'] if 'loc_super_x' in kwargs and kwargs['loc_super_x'] else 3
        loc_super_y = kwargs['loc_super_y'] if 'loc_super_y' in kwargs and kwargs['loc_super_y'] else 3

        self.floor = list()
        for y in range(self.max_map_size_y):
            floor_y = list()
            for x in range(self.max_map_size_x):
                # 初期部屋の配置
                if x == loc_prince_x and y == loc_prince_y:
                    floor_y.append(Room(x, y, prince=Prince(20, 5), is_visited=True))

                # 武器の配置
                elif x == loc_sword_x and y == loc_sword_y:
                    floor_y.append(Room(x, y, is_sword=True))

                # ポーションの配置
                elif (x == loc_potion1_x and y == loc_potion1_y) or (x == loc_potion2_x and y == loc_potion2_y):
                    floor_y.append(Room(x, y, is_potion=True))

                # stinkerの配置
                elif (x == loc_stinker1_x and y == loc_stinker1_y) or (x == loc_stinker2_x and y == loc_stinker2_y):
                    floor_y.append(Room(x, y, stinker=Stinker(25, 3)))

                # superStinkerの配置
                elif x == loc_super_x and y == loc_super_y:
                    floor_y.append(Room(x, y, stinker=Stinker(25, 3, is_super=True)))

                # その他の部屋の配置
                else:
                    floor_y.append(Room(x, y))

            self.floor.append(floor_y)

    def room(self, x, y, *args, **kwargs):
        len_x = len(self.floor)
        len_y = len(self.floor[len_x - 1]) if len_x else 0

        if 0 <= x < len_x and 0 <= y < len_y:
            room = self.floor[y][x]
        else:
            return None

        if not args and not kwargs:
            return room

        if args:
            for arg in args:
                room.destroy(arg)
            return True

        if 'set_prince' in kwargs and kwargs['set_prince']:
            prince = kwargs['set_prince']
            if not isinstance(prince, Prince):
                raise TypeError

            room.prince = prince
            return True

        if 'visit' in kwargs and kwargs['visit']:
            room.visit()
            return True

    def get_door_char(self, x, y, **kwargs):
        diff_x = kwargs['diff_x'] if 'diff_x' in kwargs and kwargs['diff_x'] else 0
        diff_y = kwargs['diff_y'] if 'diff_y' in kwargs and kwargs['diff_y'] else 0

        room = self.room(y + diff_y, x + diff_x)
        if room is None:
            return '*'

        elif room.is_locked:
            return 'L'

        else:
            return 'D'

    def get_smell_str(self, x, y):
        diff_set = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for diff in diff_set:

            room = self.room(x + diff[0], y + diff[1])
            if room:
                if room.stinker and room.stinker.is_super:
                    return '#'
                elif room.stinker:
                    return '&'
                else:
                    continue
        else:
            return ' '

    def map_print(self, debug=False):

        blank_room = [' ', ' ', ' ', ' ', ' ', ' ', ' ']
        wall_type1 = ('*', '*', '*', '*', '*', '*', '*')
        wall_type2 = ('*', ' ', ' ', ' ', ' ', ' ', '*')

        for floor_y in enumerate(self.floor):
            coordinates_y = floor_y[0]
            floor_y_room_list = floor_y[1]

            wall = [list() for _ in blank_room]

            # room OBJ内の情報取得
            for room in enumerate(floor_y_room_list):
                coordinates_x = room[0]
                room_obj = room[1]

                if room_obj.is_visited or debug:
                    if room_obj.is_sword:
                        item = '!'
                    elif room_obj.is_potion:
                        item = 'H'
                    else:
                        item = ' '

                    if room_obj.stinker:
                        if room_obj.stinker.is_super:
                            enemy = '$'
                        else:
                            enemy = 'S'
                    else:
                        enemy = ' '

                    wall_1 = list(wall_type1)
                    wall_1[3] = self.get_door_char(coordinates_x, coordinates_y, diff_y=-1)

                    wall_2 = list(wall_type2)

                    if debug:
                        wall_2[2] = str(coordinates_y)
                        wall_2[4] = str(coordinates_x)

                    wall_3 = list(wall_type2)
                    wall_3[3] = self.get_smell_str(coordinates_x, coordinates_y)

                    wall_4 = list(wall_type2)
                    wall_4[0] = self.get_door_char(coordinates_x, coordinates_y, diff_x=-1)
                    wall_4[2] = 'P' if room_obj.prince else ' '
                    wall_4[3] = '!' if room_obj.prince and room_obj.prince.is_sword else ' '
                    wall_4[4] = enemy
                    wall_4[6] = self.get_door_char(coordinates_x, coordinates_y, diff_x=1)

                    wall_5 = list(wall_type2)
                    wall_5[3] = item

                    wall_6 = list(wall_type2)

                    wall_7 = list(wall_type1)
                    wall_7[3] = self.get_door_char(coordinates_x, coordinates_y, diff_y=1)

                    wall[0].extend(wall_1)
                    wall[1].extend(wall_2)
                    wall[2].extend(wall_3)
                    wall[3].extend(wall_4)
                    wall[4].extend(wall_5)
                    wall[5].extend(wall_6)
                    wall[6].extend(wall_7)

                else:
                    wall[0].extend(blank_room)
                    wall[1].extend(blank_room)
                    wall[2].extend(blank_room)
                    wall[3].extend(blank_room)
                    wall[4].extend(blank_room)
                    wall[5].extend(blank_room)
                    wall[6].extend(blank_room)

            for w in wall:
                print(''.join(w))


if __name__ == '__main__':
    m = Map()
    m.map_print(debug=True)
