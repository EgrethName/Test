from time import perf_counter
from time import sleep

def timer():
    start = perf_counter()

    def inner():
        nonlocal start
        temp = perf_counter() - start
        start = perf_counter()

        return temp

    return inner


class Timer:
    def __init__(self):
        self.start = perf_counter()
        self.__inner = 0

    @property
    def inner(self):
        return self.__inner

    @inner.setter
    def inner(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("pls pass number")

        self.__inner = value

    def tick(self):
        temp = perf_counter() - self.start
        self.start = perf_counter()
        print(temp)
        return temp
#
#
# x = timer()
# print(x())
# sleep(3)
# print(x())

tim = Timer()
tim.tick()
sleep(3)
tim.tick()

print(tim.inner)
tim.inner = 20
print(tim.inner)
tim.inner = "asdasd"
