class rectangle:
    def __init__ (self, h = 1, w = 1):
        self.h = h
        self.w = w

    def get_perimeter(self):
        return self.h * 2 + self.w * 2

    def get_area(self):
        return self.h * self.w

    def set_width(self , width):
        self.w = width

    def set_height(self , height):
        self.h = height

    
