import math

 
class Shape():
    """
    This is a abstract class representing geometrical shape.
    """
    
    def _get_perimetr(self):
        """
        Calculates shape's perimeter.

        Returns:
            float: perimeter of the shape
        """
        pass

    
    def _get_area(self):
        """Calculates shape's area.
        Returns:
            float: area of the shape
        """
        pass

    
    def __str__(self):
        """
        Returns information about the shape as string.

        Returns:
            str: information about shape
        """
        pass


    @classmethod
    def check_below_zero(cls, *args):
        """
        Check if any of args are not below 0

        Returns:
            bool: True if any of args are not below 0

        Raises:
            ValueError: If any of the parameters is below 0.
        """
        if list(filter(lambda x: x < 0, args)):
            raise ValueError
        return True



class Circle(Shape):
    def __init__(self, r):
        self.check_below_zero(r)
        self._r = r

    def _get_perimeter(self):
        return round(2 * math.pi * self._r, 2)


    def _get_area(self):
        return round(math.pi * self._r ** 2, 2)

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, r):
        self._r = r

    def __str__(self):
        return f"Circle radius = {round(self._r, 2)}"


class Triangle(Shape):

    def __init__(self, a, b, c):

        self.check_below_zero(a, b, c)
        self._a = a
        self._b = b
        self._c = c
        self._arr = [self._a, self._b, self._c]

    def _get_area(self):

        s = (self._a + self._b + self._c) / 2
        return round(math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c)), 2)

    def _get_perimeter(self):

        return round(sum(self._arr), 2)

    def __str__(self):
        return 'Triangle, a={:0.2f}, b={:0.2f}, c={:0.2f}'.format(self._a, self._b, self._c)


class EquilateralTriangle(Triangle):

    def __init__(self, a):

        super().__init__(a, a, a)

    def __str__(self):

        return 'EquilateralTriangle, a = {:0.2f}cm'.format(self._a)


class Rectangle(Shape):

    def __init__(self, a, b):

        self.check_below_zero(a, b)
        self._a = a
        self._b = b

    def _get_area(self):

        return self._a * self._b

    def _get_perimeter(self):

        return 2 * self._a + 2 * self._b

    def __str__(self):

        return 'Rectangle, a={:0.2f}, b={:0.2f}'.format(self._a, self._b)


class Square(Rectangle):

    def __init__(self, a):

        super().__init__(a, a)

    def __str__(self):

        return 'Square, a = {:0.2f}'.format(self._a)


class ShapeList:

    def __init__(self):
        """
        Constructs a ShapeList object
        """
        self.shapes = []

    def add_shape(self, shape):
        """
        Adds shape to shapes list. This method check if shape's has Shape class as it's ancestor.
        If not it aise TypeError.
        :param shape: Shape -> Shape class object
        """
        if not isinstance(shape, Shape):
            raise TypeError
        self.shapes.append(shape)


    def __str__(self):
        return f"List objs {self.shapes}"


    def get_largest_shape_by_perimeter(self):

        perimeters = list(map(lambda x: x._get_perimeter(), self.shapes))
        return self.shapes[perimeters.index(max(perimeters))]

    def get_largest_shape_by_area(self):

        areas = list(map(lambda x: x._get_area(), self.shapes))
        return self.shapes[areas.index(max(areas))]


def generate_objects():
    arr = [Circle(12),
            Square(8),
            Triangle(5,6,8),
            EquilateralTriangle(7),
            Rectangle(5,8)]

    for i in arr:
        obj = i
        print('\n', obj,'\n')
        for i, y in enumerate(zip(['area','perimeter'],
                                [obj._get_area(),obj._get_perimeter()]),
                                 start=1):
            print(f" {i}) {y[0]} = {y[1]}cm")


if __name__ == "__main__":

    
    generate_objects()

    t = ShapeList()
    t.add_shape(Circle(90))

    print(t.shapes[0])
    
