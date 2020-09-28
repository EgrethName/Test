def nenada(func):
    def wrapper(value):
        try:
            func(value)
        except ZeroDivisionError:
            print("nenada")

    return wrapper


@nenada
def divide_1(value):
    return value / 0


@nenada
def divide_2(value):
    return value / 0


@nenada
def divide_3(value):
    return value / 0


@nenada
def divide_4(value):
    return value / 0


@nenada
def divide_5(value):
    return value / 0


divide_1(5)
divide_2(5)
divide_3(5)
divide_4(5)
divide_5(5)

divide_1 = nenada(divide_1)