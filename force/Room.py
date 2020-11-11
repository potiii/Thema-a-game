class Room:
    def __init__(self, x, y, **kwargs):
        self.is_sword = True if 'is_sword' in kwargs and kwargs['is_sword'] else False
        self.is_visited = True if 'is_visited' in kwargs and kwargs['is_visited'] else False
        self.is_potion = True if 'is_potion' in kwargs and kwargs['is_potion'] else False
        self.stinker = kwargs['stinker'] if 'stinker' in kwargs and kwargs['stinker'] else None
        self.is_locked = True if self.stinker and self.stinker.is_super else False
        self.prince = kwargs['prince'] if 'prince' in kwargs and kwargs['prince'] else None
        self.x = x
        self.y = y

        if self.is_sword and self.is_potion:
            raise ValueError

    def destroy(self, *args):
        for target in args:
            if target == 'stinker':
                self.stinker = None

            elif target == 'prince':
                self.prince = None

            elif target == 'sword':
                self.is_sword = False

            elif target == 'potion':
                self.is_potion = False

            else:
                raise ValueError

    def visit(self):
        if self.is_visited is False:
            self.is_visited = True
            return True

        return False

    def unlock(self):
        if self.is_locked:
            self.is_locked = False
            return True
        return False

    def set_prince(self, prince):
        self.prince = prince
        return True
