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
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ['*' * self.width + "\n" for _ in range(self.height)]
        
            return "".join(picture)

    def get_amount_inside(self, other):
        return int(self.get_area() / other.get_area())

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, new_side):
        self.set_width(new_side)
        self.set_height(new_side)