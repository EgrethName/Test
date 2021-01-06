class Person:
    def __init__(self, name, surname, gender="male"):
        self.name = name
        self.surname = surname
        self.gender = gender
        if self.gender != "male" and self.gender != "female":
            self.gender = "male"
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')

    def __str__(self):
        if self.gender == "male":
            return f"Гражданин {self.surname} {self.name}"
        else:
            return f"Гражданка {self.surname} {self.name}"


p1 = Person('Chuck', 'Norris')
print(p1)
p2 = Person('Mila', 'Kunis', 'female')
print(p2)
p3 = Person('Chuck', 'Norris', 'data')
print(p3)
