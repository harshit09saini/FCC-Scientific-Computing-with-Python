class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        pattern = ""
        for row in range(self.height):
            pattern += "*" * self.width + "\n"

        return pattern

    def get_amount_inside(self, shape):
        width_exterior = self.width
        height_exterior = self.height
        width_interior = shape.width
        height_interior = shape.height

        area_exterior = self.get_area()
        area_interior = shape.get_area()
        fit_shapes = int(area_exterior / area_interior)
        return fit_shapes

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)

    def set_side(self, side):
        self.width, self.height = side, side

    def set_height(self, side):
        self.set_side(side)

    def set_width(self, side):
        self.set_side(side)

    def __str__(self):
        return f"Square(side={self.width})"
