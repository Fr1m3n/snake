class PlayGround:

    def __init__(self, w, h, cs):
        self.field = []
        self.cell_size = cs
        for i in range(h):
            self.field.append([])
            for j in range(w):
                self.field[i].append(0)
        self.width = w - 2
        self.height = h - 2
        self.size = self.width, self.height
        self.clear_field()

    def clear_field(self):
        for i in range(self.height):
            for j in range(self.width):
                self.field[i][j] = 0

    def add_cell(self, where, t):
        self.field[where[0]][where[1]] = t
