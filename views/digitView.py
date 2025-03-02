from views.view import View

# Define the segments for each digit (0-9) in a 3x5 matrix
digits = {
    '0': [[1, 1, 1],
          [1, 0, 1],
          [1, 0, 1],
          [1, 0, 1],
          [1, 1, 1]],
    '1': [[0, 0, 1],
          [0, 0, 1],
          [0, 0, 1],
          [0, 0, 1],
          [0, 0, 1]],
    '2': [[1, 1, 1],
          [0, 0, 1],
          [1, 1, 1],
          [1, 0, 0],
          [1, 1, 1]],
    '3': [[1, 1, 1],
          [0, 0, 1],
          [1, 1, 1],
          [0, 0, 1],
          [1, 1, 1]],
    '4': [[1, 0, 1],
          [1, 0, 1],
          [1, 1, 1],
          [0, 0, 1],
          [0, 0, 1]],
    '5': [[1, 1, 1],
          [1, 0, 0],
          [1, 1, 1],
          [0, 0, 1],
          [1, 1, 1]],
    '6': [[1, 1, 1],
          [1, 0, 0],
          [1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]],
    '7': [[1, 1, 1],
          [0, 0, 1],
          [0, 0, 1],
          [0, 0, 1],
          [0, 0, 1]],
    '8': [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1],
          [1, 0, 1],
          [1, 1, 1]],
    '9': [[1, 1, 1],
          [1, 0, 1],
          [1, 1, 1],
          [0, 0, 1],
          [1, 1, 1]]
}

class DigitView(View):
      def __init__(self, value: int, colour: int):
            self.value = value
            self.colour = colour
            self._matrix = digits[self.value]
      
      def draw(self, x, y, canvas):
            for i, row in enumerate(self._matrix):
                  for j, val in enumerate(row):
                        if x + i >= len(canvas.matrix) or y + j >= len(canvas.matrix[0]):
                                continue

                        canvas.matrix[x + i][y + j] = val * self.colour
