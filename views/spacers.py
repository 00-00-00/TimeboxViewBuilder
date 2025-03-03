from views.view import View

# columnSpace = [[1],
#                [1],
#                [1],
#                [1],
#                [1]]

# rowSpace = [[1, 1, 1]]


class SpaceView(View):
    def __init__(self, height: int, width:int, colour: int):
        self.colour = colour
        self._matrix = [[1] * width for _ in range(height)]

    def draw(self, x, y, canvas):
        for i, row in enumerate(self._matrix):
            for j, val in enumerate(row):
                if x + i >= len(canvas.matrix) or y + j >= len(canvas.matrix[0]):
                    continue
                canvas.matrix[x + i][y + j] = val * self.colour
