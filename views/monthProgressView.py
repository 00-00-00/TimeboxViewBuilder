from views.view import View

class MonthProgressView(View):
    
    def __init__(self, month: int, completeColour: int, currentMonthColour: int):
        if month not in range(1,13):
            raise ValueError("Expectes the month to be in range [1,12]")


        matrix = [[0x000000] * 11]
        for i in range(month):
            matrix[0][i] = completeColour
        
        # 0 is Jan, input expects range [1,12]
        matrix[0][month - 1] = currentMonthColour
        super().set_matrix(matrix)