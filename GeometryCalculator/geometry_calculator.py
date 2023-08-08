class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius ** 2
