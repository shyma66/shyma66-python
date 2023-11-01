class Polygon:
    def __init__(self,sides):
        self.sides = sides
    def get_sides(self):
        return self.sides
class  Rectangle(Polygon):
    def __init__(self,width , length):
        super().__init__(4)
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.length * self.width

rectangle = Rectangle(5, 3)
print(f"A rectangle with {rectangle.get_sides()} sides.")
print(f"The area of the rectangle is {rectangle.calculate_area()}.")
