class Device:
    mask = [1, 2, 3, 4, 10]
    dict_dialog = {1: "Укажите тип устройства ", 2: "Укажите модель устройства ", 3: "Укажите производителя устройства ", 4: "Укажите цену ",
                   5: "Укажите тип принтера ", 6: "Скорость печати принтера", 7: "Формат бумаги сканера ", 8: "Тип экрана ", 9: "Диагональ экрана", 10: "Количество"}

    def dialog(self, lst):

        return{el: input(Device.dict_dialog.get(el)) for el in lst}

    def dialog_quantity(self, lst):
        while True:
            try:
                temp = Device().dialog([lst])
                # inp = temp.get(10)
                inp_data = int(temp.get(10))
                return {lst: inp_data}
            except ValueError:
                print("Fatal error. Введите число!")


class Printer(Device):
    mask = (2, 3, 4, 5, 6)

    @property
    def open_dialog(self):
        temp = {1: "Printer"}
        temp.update(Device().dialog(self.mask))
        return temp.update(Device().dialog_quantity(10))


class Scaner(Device):
    mask = (2, 3, 4, 7)

    @property
    def open_dialog(self):
        temp = {1: "Scaner"}
        temp.update(Device().dialog(self.mask))
        return temp.update(Device().dialog_quantity([10]))


class Notebook(Device):
    mask = (2, 3, 4, 8, 9)

    @property
    def open_dialog(self):
        temp = {1: "Notebook"}
        temp.update(Device().dialog(self.mask))
        return temp.update(Device().dialog_quantity([10]))
