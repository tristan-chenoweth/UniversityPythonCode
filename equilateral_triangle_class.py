import math

class eq_triangle:
    def __init__(self, side = 1):
        self.side = side

    def get_perimeter(self):
        return self.side * 3

    def get_area(self):
        return (math.sqrt(3) / 4) * (self.side ** 2)

    def set_side(self, side):
        self.side = side
