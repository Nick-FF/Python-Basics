class Car:
    speed = 60
    color = "red"
    name = "DeLorean"
    is_police = False

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, d):
        if d:
            print("Поворот направо")
        else:
            print("Поворот налево")

    def show_speed(self, spd=90):
        print("Превышение скорости")


class TownCar(Car):
    def show_speed(self, spd=60):
        if spd > 60:
            print("Превышена скорость")


class WorkCar(Car):
    def show_speed(self, spd=40):
        if spd > 40:
            print("Превышена скорость")


class SoprtCar(Car):
    pass


class PoliceCar(Car):
    pass


a = TownCar()
b = WorkCar()
c = SoprtCar()
d = PoliceCar()

a.speed = 40
a.name = "Джин"
a.color = "Yellow"
a.is_police = False

b.speed = 40
b.name = "Крепыш"
b.color = "White"
b.is_police = False

c.speed = 100
c.name = "Supreme"
c.color = "dark-red"
c.is_police = False

d.speed = 100
d.name = "Cop"
d.color = "white-blue"
d.is_police = True

a.go()
a.show_speed(a.speed)
a.turn(True)
a.stop()

b.go()
b.show_speed(b.speed)
b.turn(True)
b.stop()

c.go()
c.show_speed(c.speed)
c.turn(False)
c.stop()

d.go()
d.show_speed(d.speed)
d.turn(True)
d.stop()
