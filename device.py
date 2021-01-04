class Device:
    mask = [1, 2, 3, 4]
    # price = 0
    # name_dev = "Название"
    # type_dev = "Тип устройства"
    # manufacturer = "HP"

    # def to_store(self):
    #     Device.type_dev =
    #     Device.name_dev =
    #     Device.manufacturer =
    #     Device.price =
    #     dev_to_store = {1: Device.type_dev, 2: Device.name_dev,
    #                     3: Device.manufacturer, 4: Device.price}
    #     return dev_to_store

    def dialog(self, lst):
        dict_dialog = {1: "Укажите тип устройства ", 2: "Укажите модель устройства ", 3: "Укажите производителя устройства ", 4: "Укажите цену ",
                       5: "Укажите тип принтера ", 6: "Скорость печати принтера", 7: "Формат бумаги сканера ", 8: "Тип экрана ", 9: "Диагональ экрана"}
        return{el: input(dict_dialog.get(el)) for el in lst}


class Printer(Device):
    mask = (1, 2, 3, 4, 5, 6)

    @property
    def open_dialog(self):
        return Device().dialog(self.mask)


class Scaner(Device):
    mask = (1, 2, 3, 4, 7)

    @property
    def open_dialog(self):
        return Device().dialog(self.mask)


class Notebook(Device):
    mask = (1, 2, 3, 4, 8, 9)

    @property
    def open_dialog(self):
        return Device().dialog(self.mask)
