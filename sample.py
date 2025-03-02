from datetime import date
from layout import Row
from layout import Layout
from views.digitView import DigitView
from views.spacers import SpaceView
from viewRender import ViewRenderer


today = date.today().strftime("%d-%m")

dayTen = DigitView(today[0], 0xFF0000)
columnSpace = SpaceView(False, 0x000000)
dayUnit = DigitView(today[1], 0xFFFFFF)
rowSpace = SpaceView(True, 0x000000)
monthTen = DigitView(today[0], 0xFF0000)
columnSpace = SpaceView(False, 0x000000)
monthUnit = DigitView(today[1], 0xFFFFFF)

divider = SpaceView(isRow=False, colour=0x50C878)
fourColumn = [columnSpace] * 2

layout = Layout([
    Row([columnSpace, divider] + fourColumn + [dayTen, columnSpace, dayUnit]),
    Row([rowSpace]),
    Row( fourColumn * 2 + [monthTen, columnSpace, monthUnit])
    ])

ViewRenderer.render(layout)