class Room:
    def __init__(self, x, y, **kwargs):
        self.door = dict()
        # A:左 D:右 W:上 S:下
        self.door['A'] = False if x == 0 else True
        self.door['D'] = False if x == 4 else True
        self.door['W'] = False if y == 0 else True
        self.door['S'] = False if y == 4 else True

        self.prince = kwargs['prince'] if 'prince' in kwargs and kwargs['prince'] else None
        self.stinker = kwargs['stinker'] if 'stinker' in kwargs and kwargs['stinker'] else None

        self.is_visited = True if 'is_visited' in kwargs and kwargs['is_sword'] else False
        self.is_visited = True if x == 0 and y == 0 else False

        is_sword = True if 'is_sword' in kwargs and kwargs['is_sword'] else False
        is_potion = True if 'is_potion' in kwargs and kwargs['is_potion'] else False

        if self.stinker:
            if self.stinker.is_super:
                self.enemy = '$'
            else:
                self.enemy = 'S'
        else:
            self.enemy = ' '

        if is_potion and is_sword:
            raise ValueError

        if is_potion:
            self.item = 'H'
        elif is_sword:
            self.item = '!'
        else:
            self.item = ' '

        door = 'L' if self.stinker and self.stinker.is_super else 'D'

        wall_type1 = ('*', '*', '*', '*', '*')
        wall_type2 = ('*', ' ', ' ', ' ', '*')

        self.wall_1 = list(wall_type1)
        self.wall_1[2] = '*' if y == 0 else door

        self.wall_2 = list(wall_type2)

        self.wall_3 = list(wall_type2)
        self.wall_3[0] = door if x != 0 else '*'
        self.wall_3[1] = 'P' if self.prince else ' '
        self.wall_3[2] = '!' if self.prince and self.prince.is_sword else ' '
        self.wall_3[3] = self.enemy
        self.wall_3[4] = door if x != 4 else '*'

        self.wall_4 = list(wall_type2)
        self.wall_4[2] = self.item

        self.wall_5 = list(wall_type1)
        self.wall_5[2] = '*' if y == 4 else door

    def destroy_item(self):
        self.item = ' '
        self.wall_4[2] = self.item

    def destroy_wall_3(self, *args):
        for target in args:
            if target is 'prince':
                self.wall_3[1] = ' '
            elif target is 'sword':
                self.wall_3[2] = ' '
            elif target is 'enemy':
                self.wall_3[3] = ' '
            else:
                pass

    def visit(self):
        if self.is_visited is False:
            self.is_visited = True
