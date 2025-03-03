from datetime import date
from layout import Row
from layout import Layout
from views.digitView import DigitView
from views.spacers import SpaceView
from viewRender import ViewRenderer
from views.weekView import WeekView
from views.monthProgressView import MonthProgressView


today = date.today().strftime("%d-%m")

dayTen = DigitView(today[0], 0xFFFFFF)
columnSpace = SpaceView(height=5, width=1, colour=0x000000)
dayUnit = DigitView(today[1], 0xFFFFFF)
rowSpace = SpaceView(height = 1, width=11, colour=0x000000)

day_number = date.today().isoweekday()
weekView = WeekView(day_number,0x00C000)

month = date.today().month
progressMonthView = MonthProgressView(
    month,
    completeColour = 0x00C000, 
    currentMonthColour = 0x2196F3
    )

layout = Layout([
    Row([SpaceView(height=2, width=2, colour=0x000000), weekView]),
    Row([SpaceView(height=1, width=11, colour=0x000000)]),
    Row([dayTen, SpaceView(1,1, 0x000000), dayUnit]),
    Row([SpaceView(height=1, width=11, colour=0x000000)]),
    Row([progressMonthView])
])

ViewRenderer.render(layout)