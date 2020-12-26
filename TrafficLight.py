import time


class TrafficLight:
    # атрибуты класса
    __color = {1: 'red', 2: 'yellow', 3: 'green'}
    # методы класса

    def running(self, y=2):
        print(self.__color[1])
        time.sleep(y + 10)
        print(self.__color[2])
        time.sleep(y)
        print(self.__color[3])


g = TrafficLight()
g.running()
