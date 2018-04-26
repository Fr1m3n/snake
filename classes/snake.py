from classes import playground


class Snake:

    def __init__(self):
        self.start_cell = [0, 0]
        self.body = [self.start_cell, ]
        self.direction = 'RIGHT'
        self.length = 5

    def remove_tail(self):
        self.body.pop(0)

    def add_head(self):
        next_cell = self.body[-1].copy()
        if (self.direction == 'LEFT'):
            next_cell[0] -= 1
        elif (self.direction == 'RIGHT'):
            next_cell[0] += 1
        elif (self.direction == 'TOP'):
            next_cell[1] -= 1
        elif (self.direction == 'BOT'):
            next_cell[1] += 1
        self.body.append(next_cell)

    def change_directory(self, dir):
        now = self.direction
        if not ((now == 'LEFT' and dir == 'RIGHT') or (now == 'TOP' and dir == 'BOT') or
                (now == 'RIGHT' and dir == 'LEFT') or (now == 'BOT' and dir == 'TOP')):
            self.direction = dir
