from layout import Row
from layout import Layout
from views.digitView import DigitView
from views.spacers import SpaceView
from transformer.pngTransformer import PngTransformer
from viewRender import ViewRenderer

digitView = DigitView('9', 0xFF0000)
columnSpace = SpaceView(False, 0x000000)
digitView2 = DigitView('8', 0xFFFFFF)
rowSpace = SpaceView(True, 0x000000)

fourColumn = [columnSpace] * 4

layout = Layout([
    Row([columnSpace, columnSpace, columnSpace, columnSpace, digitView2, columnSpace, digitView2]),
    Row([rowSpace]),
    Row(fourColumn  + [digitView, columnSpace, digitView2])
    ])

ViewRenderer.render(layout)