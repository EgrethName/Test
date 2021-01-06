class Square:
    def __init__(self, s):
        self.side = s

    def area(self):
        return self.side**2


b = Square(6)
print(b.area)
