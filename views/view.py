class View:

    def __init__(self):
        self._matrix = []

    def set_matrix(self, matrix):
        self._matrix = matrix

    def get_height(self):
        return len(self._matrix)
    
    def get_width(self):
        return len(self._matrix[0])
    
    def draw(self, x, y, canvas):
        for i, row in enumerate(self._matrix):
            for j, val in enumerate(row):
                if x + i >= len(canvas.matrix) or y + j >= len(canvas.matrix[0]):
                    continue

                canvas.matrix[x + i][y + j] = val