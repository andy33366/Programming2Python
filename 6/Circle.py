from Shape import Shape

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    def area(self):
        return 3.14 * self.raduis**2
