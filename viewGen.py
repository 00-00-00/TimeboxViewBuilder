from canvas import Canvas
from layout import Row
from layout import Layout
from views.digitView import DigitView
from views.spacers import SpaceView
from transformer.pngTransformer import PngTransformer

# Create the canvas 11x11
canvas = Canvas(11, 11)

digitView = DigitView('9', 0xFF0000, canvas)
columnSpace = SpaceView(False, 0x000000, canvas)
digitView2 = DigitView('8', 0xFFFFFF, canvas)
rowSpace = SpaceView(True, 0x000000, canvas)
characterView = DigitView(':', 0xFF0000, canvas)


layout = Layout([
    Row([columnSpace, columnSpace, columnSpace, columnSpace, digitView2, columnSpace, digitView2]),
    Row([rowSpace]),
    Row([columnSpace, characterView, digitView, columnSpace, digitView2])
    ])

layout.draw(0,0)
canvas.draw()  # Just for debug output

print("RGB Image saved as output.png")

imageFile = PngTransformer().generateFromCanvas(canvas)
imageFile.save("output.png")