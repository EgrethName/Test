class Zebra:
    cnt = 0

    def which_stripe(self):
        if self.cnt % 2 == 0:
            print("Полоска белая")
            self.cnt += 1
        else:
            print("Полоска черная")
            self.cnt += 1


z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()

z2 = Zebra()
z2.which_stripe()