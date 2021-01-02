class Complex:
    def __init__(self, a, b):
        self.c = a, b
        self.a = a
        self.b = b

    def __str__(self):
        return f"Результат {self.c[0]} {self.c[1]}j"

    def __add__(self, other):

        return [sum(el) for el in zip(self.c, other.c)]

    def __mul__(self, other):
        return [self.c[0]*other.c[0]+(-1*self.c[1]*other.c[1]), self.c[0]*other.c[1]+(self.c[1]*other.c[0])]


print("Умножение  комплексных чисел")

a1 = int(input("Задайте действительную часть первого числа "))
b1 = int(input("Задайте мнимую часть первого числа "))
a2 = int(input("Задайте действительную часть второго числа "))
b2 = int(input("Задайте мнимую часть второго числа "))


c1 = Complex(a1, b1)
c2 = Complex(a2, b2)
# d = c1 + c2
d = c1 * c2
c3 = Complex(*d)
print(c3)
