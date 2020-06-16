from room import Room
from character import Stinker, Prince


# prince hp = 20
# stinker hp = 25
# prince dmg = 5
# sword dmg  +10
# stinker dmg = 3

class Map:
    def __init__(self):
        self.floor = list()
        for y in range(5):
            floor_y = list()
            for x in range(5):
                if x == 0 and y == 0:
                    floor_y.append(Room(x, y, prince=Prince(20, 5), is_visit=True))
                elif (x == 1 and y == 4) or (x == 2 and y == 1):
                    floor_y.append(Room(x, y, stinker=Stinker(25, 3)))
                elif x == 3 and y == 3:
                    floor_y.append(Room(x, y, stinker=Stinker(25, 3, is_super=True)))
                elif x == 0 and y == 3:
                    floor_y.append(Room(x, y, is_sword=True))
                elif (x == 4 and y == 2) or (x == 2 and y == 4):
                    floor_y.append(Room(x, y, is_potion=True))
                else:
                    floor_y.append(Room(x, y))
            self.floor.append(floor_y)

    def map_print(self):
        blank_wall = [' ', ' ', ' ', ' ', ' ']

        for floor_y in self.floor:
            wall = [list() for _ in range(5)]
            for room in floor_y:
                if room.is_visited or True:
                    wall[0].extend(room.wall_1)
                    wall[1].extend(room.wall_2)
                    wall[2].extend(room.wall_3)
                    wall[3].extend(room.wall_4)
                    wall[4].extend(room.wall_5)

                else:
                    wall[0].extend(blank_wall)
                    wall[1].extend(blank_wall)
                    wall[2].extend(blank_wall)
                    wall[3].extend(blank_wall)
                    wall[4].extend(blank_wall)

            for w in wall:
                print(''.join(w))


if __name__ == '__main__':
    m = Map()
    m.map_print()
