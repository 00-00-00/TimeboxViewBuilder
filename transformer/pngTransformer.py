from transformer.colour import HexToRGBTransformer
from PIL import Image
import numpy as np

class PngTransformer:
    
    def generateFromCanvas(self, canvas):
        colourTransformedMatrix = [[HexToRGBTransformer.transform(hexValue) for hexValue in row] for row in canvas.matrix ]
        array = np.array(colourTransformedMatrix, dtype=np.uint8)
        return Image.fromarray(array)