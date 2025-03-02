from canvas import Canvas
from layout import Row
from layout import Layout
from views.digitView import DigitView
from views.spacers import SpaceView
from PIL import Image
import numpy as np

# Create the canvas 11x11
canvas = Canvas(11, 11)
digitView = DigitView('9', 255, canvas)
columnSpace = SpaceView(False, 0, canvas)
digitView2 = DigitView('8', 255, canvas)
rowSpace = SpaceView(True, 0, canvas)


row1 = Row(canvas)
row1.addViews([digitView2, columnSpace, digitView2, columnSpace, digitView2])
row2 = Row(canvas)
row2.addViews([rowSpace])
row3 = Row(canvas)
row3.addViews([digitView, columnSpace, digitView2])

layout = Layout(canvas)
layout.addViews([row1, row2, row3])

layout.draw(0,0)
canvas.draw()

array = np.array(canvas.matrix, dtype=np.uint8)
image = Image.fromarray(array)
image.save("output.png")

print("RGB Image saved as output.png")