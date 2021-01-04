from device import Printer, Scaner, Notebook


class Store:
    store_dict = {}

    def add_device(self, dev):
        if dev == "1":
            Store.store_dict.update(Printer().open_dialog)
        if dev == "2":
            Store.store_dict.update(Scaner().open_dialog)
        if dev == "3":
            Store.store_dict.update(Notebook().open_dialog)
