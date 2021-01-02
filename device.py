class Device:
    price = 0
    name_d = "Название"
    type_d = "Тип устройства"
    manufacturer = "HP"

    def to_store():
        dev_to_store = {1: type_d, 2: name_d, 3: manufacturer, 4: price}


class Printer(Device):
    type_printer = "Laser"
    speed_list_min = 100


class Scaner(Device):
    format_scaner = "A4"


class Notebook(Device):
    type_screen = "OLED"
    size_screen_inch = 17
