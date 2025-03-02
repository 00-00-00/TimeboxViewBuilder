from canvas import Canvas
from layout import Row
from layout import Layout
from model.colour import HexToRGBTransformer
from views.digitView import DigitView
from views.spacers import SpaceView
from PIL import Image
import numpy as np

# Create the canvas 11x11
canvas = Canvas(11, 11)

digitView = DigitView('9', 0xFF0000, canvas)
columnSpace = SpaceView(False, 0x000000, canvas)
digitView2 = DigitView('8', 0xFFFFFF, canvas)
rowSpace = SpaceView(True, 0x000000, canvas)


layout = Layout([
    Row([digitView2, columnSpace, digitView2, columnSpace, digitView2]),
    Row([rowSpace]),
    Row([digitView, columnSpace, digitView2])
    ])

layout.draw(0,0)
canvas.draw()

colourTransformedMatrix = [[HexToRGBTransformer.transform(hexValue) for hexValue in row] for row in canvas.matrix ]
array = np.array(colourTransformedMatrix, dtype=np.uint8)
image = Image.fromarray(array)
image.save("output.png")

print("RGB Image saved as output.png")