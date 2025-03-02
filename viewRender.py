from canvas import Canvas
from layout import Row
from layout import Layout
from views.digitView import DigitView
from views.spacers import SpaceView
from transformer.pngTransformer import PngTransformer

class ViewRenderer:

    def render(layout):
        # Create the canvas 11x11
        canvas = Canvas(11, 11)

        layout.draw(0,0, canvas)
        canvas.draw()  # Just for debug output

        print("RGB Image saved as output.png")

        imageFile = PngTransformer().generateFromCanvas(canvas)
        imageFile.save("output.png")