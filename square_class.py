class square:
    def __init__(self, side = 1):
        self.side = side

    def get_perimeter(self):
        return 4 * self.side

    def get_area(self):
        return self.side ** 2

    def set_side(self, side):
        self.side = side
        
