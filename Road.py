class Road:
    __length = 0
    __width = 0

    def __init__(self, l=10, w=20, m=25, laying=5):
        self.__length = l
        self.__width = w
        self.__mass = m
        self.__laying = laying
        print(
            f"Масса асфальта равна {self.__length * self.__width * self.__mass * self.__laying/1000}тонн")
        print(f"Масса асфальта равна {l*w*m*laying/1000}тонн")


mass = Road(20, 5000, 25, 5)
