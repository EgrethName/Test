class iterable:
    def __init__(self):
        self.a = []
        self.i

    def __iter__(self):
        return self

    def __next__(self):
        return self.a

iterable_instance = iterable()

iter(iterable_instance)