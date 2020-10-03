class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def property_perimeter(self):
        self.perimeter = self.__a + self.__b + self.__c
        return self.perimeter

    @property_perimeter.setter
    def property_perimeter(self, sides):
        if len(sides) == 3:
            self.__a = sides[0]
            self.__b = sides[1]
            self.__c = sides[2]
        else:
            raise Exception('Input three sides')

    @property
    def property_area(self):
        self.perimeter = self.__a + self.__b + self.__c
        self.perim_2 = self.perimeter / 2
        area = (self.perim_2 * (self.perim_2 - self.__a) * (self.perim_2 - self.__b) * (self.perim_2 - self.__c)) ** 0.5
        return area

    @property_area.setter
    def property_area(self, sides):
        try:
            if len(sides) == 3:
                self.__a = sides[0]
                self.__b = sides[1]
                self.__c = sides[2]
            else:
                raise Exception('Input three sides')
        except TypeError:
            print('Input three sides')


t = Triangle(1, 1, 1)
print(t.property_area)
print(t.property_perimeter)
t.property_area = (2, 2, 2)
t.property_perimeter = (2, 2, 2)
print(t.property_area)
print(t.property_perimeter)
