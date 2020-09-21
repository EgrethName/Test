class Counter:
    def start_from(self, start=0):
        self.start_number = start

    def increment(self):
        self.start_number += 1

    def display(self):
        print("Текущее значение счетчика = {}".format(self.start_number))

    def reset(self):
        self.start_number = 0


c1 = Counter()
c1.start_from()
c1.increment()
c1.display()
c1.increment()
c1.display()
c1.reset()
c1.display()

print(c1.__dict__)
