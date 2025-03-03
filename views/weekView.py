from views.view import View

class WeekView(View):

    weekView = [
        [0xFF0000, 0xFFFFFF, 0xFFFFFF, 0xFFFFFF, 0xFFFFFF, 0xFFFFFF, 0xFF0000],
        [0xFF0000, 0xFFFFFF, 0xFFFFFF, 0xFFFFFF, 0xFFFFFF, 0xFFFFFF, 0xFF0000]
    ]

    def __init__(self, dayOfWeek: int, highlightColour: int):

        if dayOfWeek not in range (0,7):
            raise ValueError("Day of week must be in range [0,7]")


        self.weekView[1][dayOfWeek] = highlightColour 
        super().set_matrix(self.weekView)
