class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)

    def __str__(self):
        if len(self.values) > 0:
            return f"Вектор{tuple(sorted(self.values))}"
        else:
            return "Пустой вектор"


v1 = Vector([4, 5], 'hello', 3, -1.5, 1, 2)
print(v1)
v2 = Vector()
print(v2)
