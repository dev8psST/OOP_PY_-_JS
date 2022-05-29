#pytest -vv test.py
import unittest
import math
from my_code import *



class CircleTester(unittest.TestCase):

    def test_constructor(self):
        c = Circle(3)
        self.assertEqual(c._r, 3, "Wrong radius")

    def test_value_error(self):
        with self.assertRaises(ValueError,
                               msg="Circle radius can't be negative"):
            Circle(-1)

    def test_area(self):
        r = 3
        c = Circle(r)
        area = math.pi * r ** 2
        self.assertEqual(c._get_area(), round(area, 2))

    def test_perimeter(self):
        r = 3
        c = Circle(r)
        perimeter = 2 * math.pi * r
        self.assertEqual(c._get_perimeter(), round(perimeter,2))


class TriangleTester(unittest.TestCase):

    def test_constructor(self):
        t = Triangle(2, 4, 5)
        self.assertEqual((t._a, t._b, t._c), (2, 4, 5))

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Triangle(-1, 1, 1)

    def test_area(self):
        a = 2
        b = 4
        c = 5
        t = Triangle(a, b, c)
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        self.assertEqual(t._get_area(), round(area, 2))

    def test_perimeter(self):
        a = 2
        b = 4
        c = 5
        t = Triangle(a, b, c)
        perimeter = a + b + c
        self.assertEqual(t._get_perimeter(), perimeter)


class EquilateralTriangleTester(unittest.TestCase):

    def test_constructor(self):
        t = EquilateralTriangle(2)
        self.assertEqual((t._a, t._b, t._c), (2, 2, 2))

    def test_value_error(self):
        with self.assertRaises(ValueError):
            EquilateralTriangle(-1)

    def test_area(self):
        a = b = c = 2
        t = EquilateralTriangle(a)
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        self.assertEqual(t._get_area(), round(area, 2))

    def test_perimeter(self):
        a = 2
        t = EquilateralTriangle(a)
        perimeter = 3*a
        self.assertEqual(t._get_perimeter(), perimeter)


class RectangleTester(unittest.TestCase):

    def test_constructor(self):
        r = Rectangle(2, 3)
        self.assertEqual((r._a, r._b), (2, 3))

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)

    def test_area(self):
        a = 2
        b = 3
        r = Rectangle(a, b)
        area = a * b
        self.assertEqual(r._get_area(), area)

    def test_perimeter(self):
        a = 2
        b = 3
        r = Rectangle(a, b)
        perimeter = 2*a + 2*b
        self.assertEqual(r._get_perimeter(), perimeter)


class SquareTester(unittest.TestCase):

    def test_constructor(self):
        s = Square(2)
        self.assertEqual((s._a, s._b), (2, 2))

    def test_value_error(self):
        with self.assertRaises(ValueError):
            Square(-1)
            Square(-90)

    def test_area(self):
        a = 2
        s = Square(a)
        area = a**2
        self.assertEqual(s._get_area(), area)

    def test_perimeter(self):
        a = 2
        s = Square(a)
        perimeter = a*4
        self.assertEqual(s._get_perimeter(), perimeter)






class ShapeListTester(unittest.TestCase):

    def test_constructor(self):
        sl = ShapeList()
        self.assertIsInstance(sl.shapes, list)

    def test_add_shape(self):
        sl = ShapeList()
        c = Circle(2)
        sl.add_shape(c)
        self.assertEqual(sl.shapes[0], c)

    def test_type_error(self):
        sl = ShapeList()
        with self.assertRaises(TypeError, msg="This Shape is wrong"):
            sl.add_shape("Fail add shape")



    def test_largest_perimeter(self):
        sl = ShapeList()
        s = Square(5)
        t = Triangle(2, 4, 5)
        c = Circle(3)
        
        sl.add_shape(s)
        sl.add_shape(t)
        sl.add_shape(c)
        self.assertEqual(sl.get_largest_shape_by_perimeter(), s)

    def test_largest_area(self):
        sl = ShapeList()
        s = Square(5)
        t = Triangle(2, 4, 5)
        c = Circle(3)
        
        sl.add_shape(s)
        sl.add_shape(t)
        sl.add_shape(c)
        self.assertEqual(sl.get_largest_shape_by_area(), c)





def main():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    main()
