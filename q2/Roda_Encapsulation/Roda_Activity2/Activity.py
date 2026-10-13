
class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.__width = new_width
        else:
            print("Width must be greater than zero.")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.__height = new_height
        else:
            print("Height must be greater than zero.")

    def get_area(self):
        return self.__width * self.__height


my_rectangle = Rectangle(8, 5)

print("Original width:", my_rectangle.width)
print("Original height:", my_rectangle.height)
print("Area:", my_rectangle.get_area())

my_rectangle.width = 10
my_rectangle.height = 6

print("\nUpdated width:", my_rectangle.width)
print("Updated height:", my_rectangle.height)
print("New area:", my_rectangle.get_area())
