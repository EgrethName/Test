class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__sides = [a, b, c]

    @property
    def side_a(self):
        return self.__a

    @side_a.setter
    def side_a(self, value_a):
        self.__a = value_a

    @property
    def side_b(self):
        return self.__b

    @side_b.setter
    def side_b(self, value_b):
        self.__b = value_b

    @property
    def side_c(self):
        return self.__c

    @side_c.setter
    def side_c(self, value_c):
        self.__c = value_c

    @property
    def perimeter(self):
        return self.__a + self.__b + self.__c

    @property
    def area(self):
        self.perim_2 = self.perimeter/ 2
        area = (self.perim_2 * (self.perim_2 - self.__a) * (self.perim_2 - self.__b) * (self.perim_2 - self.__c)) ** 0.5
        return area


class TriangleSides:
    def __init__(self, a, b, c):
        self.__sides = [a, b, c]

    @property
    def sides(self):
        return self.__sides

    @sides.setter
    def sides(self, value):
        if isinstance(value, list) or isinstance(value, tuple):
            self.sides = value
        else:
            raise ValueError('передайте список или кортеж')

    @property
    def perimeter(self):
        return sum(self.__sides)

    @property
    def area(self):
        self.perim_2 = self.perimeter/ 2
        area = (self.perim_2 * (self.perim_2 - self.sides[0]) * (self.perim_2 - self.sides[1]) * (self.perim_2 - self.sides[2])) ** 0.5
        return area


t = Triangle(1, 1, 1)
print(t.area)
print(t.perimeter)
t.side_a = 1
t.side_b = 1
t.side_c = 1
print(t.area)
print(t.perimeter)
