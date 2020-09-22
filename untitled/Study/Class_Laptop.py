class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = self.brand + " " + self.model


laptop1 = Laptop('hp', '15-bw0xx', 57000)
laptop2 = Laptop('asus', '15v4700', 48000)
print(laptop1.laptop_name)
print(laptop2.laptop_name)
