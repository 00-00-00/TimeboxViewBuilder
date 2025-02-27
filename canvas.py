class Canvas:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.matrix = [[0 for _ in range(width)] for _ in range(height)]

    def draw(self):
        for row in self.matrix:
            print("   ".join(map(str, row)))