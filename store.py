from device import Printer, Scaner, Notebook


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
            el.get(10) for el in Store.store_dict.values() if el == Printer().open_dialog
        if rqst == "2":
            Store.store_dict.update(Scaner().open_dialog)
        if rqst == "3":
            Store.store_dict.update(Notebook().open_dialog)
         # если все вери гуд, то запрашиваем количество
            try:
                inp_data = int(input("Сколько выдать со склада? "))
                a.append(inp_data)
            except ValueError as alarm:
                print("Fatal error. Введите число!")
