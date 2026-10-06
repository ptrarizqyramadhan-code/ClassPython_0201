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


# Input
length = float(input("Enter the length: "))
while length == 0:
    print("Input cannot be 0!")
    length = float(input("Enter the length: "))

width = float(input("Enter the width: "))
while width == 0:
    print("Input cannot be 0!")
    width = float(input("Enter the width: "))


# Membuat object dari class Rectangle
rectangle = Rectangle(length, width)

# Menampilkan object menggunakan __str__
print(rectangle)

# Memanggil function circumference
print("Circumference:", rectangle.circumference(), "cm")

# Memanggil function area
print("Area:", rectangle.area(), "cm²")