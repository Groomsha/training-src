"""
Класс Rectangle является суперклассом, а Square является подклассом, поскольку методы Square наследуются от Rectangle,
то мы можем вызвать метод __init__() суперкласса (Rectangle.__ init__()) из класса Square используя функцию super().
"""


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, length):
        # Для квадрата просто нужно передать один параметр length.
        # При вызове 'super().__init__()' установим атрибуты 'length' и 'width'.
        super().__init__(length, length)


# Класс Square явно не реализует метод area() и будет использовать его из суперкласса Rectangle:
sqr = Square(4)
print("Area of Square is:", sqr.area())

rect = Rectangle(2, 4)
print("Area of Rectangle is:", rect.area())
