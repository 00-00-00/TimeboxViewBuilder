from canvas import Canvas

class View:

    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self._matrix = []

    def set_matrix(self, matrix):
        self._matrix = matrix

    def get_height(self):
        return len(self._matrix)
    
    def get_width(self):
        return len(self._matrix[0])
    
    def draw(self, x, y):
        for i, row in enumerate(self._matrix):
            for j, val in enumerate(row):
                if x + i >= len(self.canvas.matrix) or y + j >= len(self.canvas.matrix[0]):
                    continue

                self.canvas.matrix[x + i][y + j] = val