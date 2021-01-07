from device import Printer
from device import Scaner
from device import Notebook


class Store:
    store_dict = {}
    flag = 0

    def add_device(self, dev):
        if dev == "1":
            Store.store_dict.update(Printer().open_dialog)

        if dev == "2":
            Store.store_dict.update(Scaner().open_dialog)
        if dev == "3":
            Store.store_dict.update(Notebook().open_dialog)

    def get_device(self, rqst):
        if rqst == "1":
            print(el.values()
                  for el in Store.store_dict if el.values()[0] == "Printer")

        if rqst == "2":
            Store.store_dict.update(Scaner().open_dialog)
        if rqst == "3":
            Store.store_dict.update(Notebook().open_dialog)
         # если все вери гуд, то запрашиваем количество
            try:
                inp_data = int(input("Сколько выдать со склада? "))
            except ValueError:
                print("Fatal error. Введите число!")
