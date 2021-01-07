from store import Store
from catchexc import CatchError


class Request:

    try:
        while True:
            q = input(
                "Внести на склад нажми '1', передать со склада нажми '2', для завершения введи 'stop'")
            if q == "stop":
                raise CatchError("Ввод данных остановлен")
            if q == "1":
                q1 = input(
                    "Выберите устройство 1 - Принтер, 2 - Сканер, 3 - Ноутбук ")
                s = Store()
                s.add_device(q1)
                print(s.store_dict)
                # добавить сравнение уже существующего, чтобы просто увеличить занчение количества.
            if q == "2":
                q2 = input(
                    "Выберите устройство 1 - Принтер, 2 - Сканер, 3 - Ноутбук ")
                s1 = Store()
                s1.get_device(q2)
                # если все вери гуд, то запрашиваем количество
            try:
                inp_data = int(inp_data)
                a.append(inp_data)
                i += 1
            except ValueError as alarm:
                print("Fatal error. Введите число!")

    except CatchError as err:
        print(err)
    finally:
        print(a)
