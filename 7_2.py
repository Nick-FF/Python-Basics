from abc import ABC, abstractmethod


class Closes(ABC):
    def __init__(self, arg):
        self.arg = arg

    @abstractmethod
    def calc_material(self):
        return 0.5 * self.arg


class Coat(Closes):
    @property
    def calc_material(self):
        return self.arg/6.5 + 0.5


class Suit(Closes):
    @property
    def calc_material(self):
        return 2 * self.arg + 0.3


q1 = int(input("Введите рост для костюма "))
q2 = int(input("Введите размер для польто "))

if q2:
    a = Coat(q2)
    t1 = a.calc_material

if q1:
    b = Suit(q1)
    t2 = b.calc_material


print(f"Потребуется материала {t1 + t2}")
