class Rectangle:
    # Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Function untuk menghitung circumference / keliling
    def circumference(self):
        return 2 * (self.length + self.width)

    # Function untuk menghitung luas
    def area(self):
        return self.length * self.width

    # Function __str__
    def __str__(self):
        return f"Rectangle, {self.length} cm long, and {self.width} cm wide"

