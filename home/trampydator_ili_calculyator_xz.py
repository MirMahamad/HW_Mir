class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def __add__(self):
        print(f'{self.n1 + self.n2}')

    def __sub__(self):
        print(f"{self.n1 - self.n2}")

    def __mul__(self):
        print(f"{self.n1 * self.n2}")

    def __truediv__(self):
        print(f'{self.n1 / self.n2}')

a = Calculator(7, 7)
a.__add__()
a.__sub__()
a.__mul__()
a.__truediv__()