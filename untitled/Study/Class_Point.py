class Point:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, point_2):
        if isinstance(point_2, Point):
            x = point_2.x - self.x
            y = point_2.y - self.y
            c = (x**2 + y**2) ** 0.5
            return c
        else:
            print("Передана не точка")
            return


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2)
g = p1.get_distance(10)
print(d)
