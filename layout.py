from canvas import Canvas
from views.view import View

class Row(View):
    def __init__(self):
        self.__height = 0
        self.__width = 0

    def __init__(self, views):
        self.__views = views
        self.__measure()
    
    def addViews(self, views):
        self.__views = views
        self.__measure()

    def __measure(self):
        height = 0
        for view in self.__views:
            if (view.get_height() > height):
                height = view.get_height()
            
        self.__height = height

        width = 0
        for view in self.__views:
            width += view.get_width()

        self.__width = width

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def draw(self, x, y):
        offset = y
        for view in self.__views:
            view.draw(x, offset)
            offset += view.get_width()
    
class Layout(View):
    def __init__(self):
        self.__height = 0
        self.__width = 0

    def __init__(self, rows):
        self.__views = rows
        self.__measure()

    def addViews(self, rows):
        self.__views = rows
        self.__measure()

    def __measure(self):
        width = 0
        for view in self.__views:
            if (view.get_width() > width):
                width = view.get_width()
            
        self.__width = width

        height = 0
        for view in self.__views:
            height += view.get_height()

        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def draw(self, x, y):
        offset = x
        for view in self.__views:
            view.draw(offset, y)
            offset += view.get_height()