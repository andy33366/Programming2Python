from Rectangle import Rectangle
from Shape import Shape

class Square(Shape):
    def __init__(self, x, y, length):
        #if using rectangls --> super().__init__(x, y, length, length)
        super().__init__(x, y)
        self.length = length

    def area(self):
        return self.length **2
