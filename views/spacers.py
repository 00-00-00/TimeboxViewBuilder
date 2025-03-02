from views.view import View

columnSpace = [[0],
               [0],
               [0],
               [0],
               [0]]

rowSpace = [[0, 0, 0]]


class SpaceView(View):
    def __init__(self, isRow: bool, colour: int):
        self.colour = colour
        self._matrix = rowSpace if isRow else columnSpace

    def draw(self, x, y, canvas):
        for i, row in enumerate(self._matrix):
            for j, val in enumerate(row):
                if x + i >= len(canvas.matrix) or y + j >= len(canvas.matrix[0]):
                    continue
                canvas.matrix[x + i][y + j] = val * self.colour
