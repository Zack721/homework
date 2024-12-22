class Shape:
    def __init__(s, width, height):
        s.width_ = width
        s.height_ = height

    
class Circle(Shape):
    def __init__(s, width, height):
        super().__init__(width, height)
        s.diameter = width
        s.width_ = height


    def Circumference(s):
        print(f"The circles cirumference is {s.diameter * 3.14}")

    def Area(s):
        print(f"The area of the circle is {3.14 * 0.25 * (s.diameter)**2}")


class Triangle(Shape):
    def __init__(s, width, height, side_length):
        super().__init__(width, height )
        s.side_length_ = side_length

    def Perimeter(s):
        print(f"The perimeter of the triangle is {s.side_length_ * 2 + s.width_}")

    def Area(s):
        print(f"The area of the triangle is {s.width_ * s.height_ * 0.5}")

class Square(Shape):
    def __init__(s, width, height):
        super().__init__(width, height)

    def Perimeter(s):
        print(f"The perimeter of the square is {4* s.width_}")
    
    def Area(s):
        print(f"The area of the square is {s.width_ * s.width_}")



def main():
    circle1 = Circle(10, 12)
    circle1.Circumference()
    circle1.Area()

    triangle1 = Triangle(10, 15, 12)
    triangle1.Perimeter()
    triangle1.Area()

    square1 = Square(77, 77)
    square1.Perimeter()
    square1.Area()

main()