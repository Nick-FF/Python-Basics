dict_dialog = {1: "Укажите тип устройства ", 2: "Укажите название устройства ", 3: "Укажите производителя устройства ", 4: "Укажите цену ",
               5: "Укажите тип принтера ", 6: "Скорость печати принтера ", 7: "Формат бумаги сканера ", 8: "Тип экрана ", 9: "Диагональ экрана"}
lst = [1, 3, 4, 6, 7]
# q1 = input([dict_dialog.get(el) for el in lst])

# for el in lst:
#     q1 = input(dict_dialog.get(el))
f = {el: input(dict_dialog.get(el)) for el in lst}
el.get(10) for el in dict_dialog.values() if el ==
