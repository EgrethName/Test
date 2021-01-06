class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, new_dollars):
        if isinstance(new_dollars, int) and new_dollars >= 0:
            self.total_cents = new_dollars * 100 + self.cents
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, new_cents):
        if isinstance(new_cents, int) and 0 <= new_cents < 100:
            self.total_cents = self.dollars * 100 + new_cents
        else:
            print("Error cents")

    def __str__(self):
        return f"Ваше состояние составляет {self.total_cents // 100} долларов {self.total_cents % 100} центов"


Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
