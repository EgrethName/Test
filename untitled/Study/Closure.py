def multiplier_of(value):
    number = value

    def multiply(x):
        print(number * x)

    return multiply


multiplywith5 = multiplier_of(5)
multiplywith5(0)
