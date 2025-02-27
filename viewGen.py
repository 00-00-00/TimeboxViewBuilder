from canvas import Canvas
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

digitView.draw(0,0)
columnSpace.draw(0,digitView.get_width())
digitView2.draw(0,digitView.get_width() + columnSpace.get_width())
columnSpace.draw(0,digitView.get_width() + columnSpace.get_width() + digitView2.get_width())
digitView2.draw(0,digitView.get_width() + columnSpace.get_width() + digitView2.get_width() + columnSpace.get_width())

rowSpace.draw(digitView.get_height(),0)
digitView.draw(digitView.get_height() + rowSpace.get_height(),0)
digitView2.draw(digitView.get_height() + rowSpace.get_height(), digitView.get_width() + columnSpace.get_width())

canvas.draw()

array = np.array(canvas.matrix, dtype=np.uint8)
image = Image.fromarray(array)
image.save("output.png")

print("RGB Image saved as output.png")