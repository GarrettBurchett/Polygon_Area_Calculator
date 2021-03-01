class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
    def set_height(self, new_height):
        self.height = new_height

    def set_width(self, new_width):
        self.width = new_width

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * self.height + 2 * self.width

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        for _ in range(self.height):
            return '*' * self.width

    def get_amount_inside(self, other):
        return int(self.get_area() / other.get_area())

class Square(Rectangle):
    pass