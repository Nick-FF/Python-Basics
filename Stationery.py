class Stationery:
    title = "paint"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Ручка")


class Pencil(Stationery):
    def draw(self):
        print("Карандаш")


class Handle(Stationery):
    def draw(self):
        print("Маркер")


a = Pen()
b = Pencil()
c = Handle()

a.draw()
b.draw()
c.draw()
