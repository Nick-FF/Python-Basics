import store
import catchexc


class Request:

    try:
        while True:
            q = input(
                "Внести на склад нажми '1', передать со склада нажми '2', для завершения введи 'stop'")
            if q == "stop":
                raise CatchError("Ввод данных остановлен")
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
    while True:

        if q1 == "stop":
            break
        q1 = input("Выберите устройство 1 - Принтер, 2 - Сканер, 3 - Ноутбук ")
        s = Store()
        s.add_device(q1)
        print(s.store_dict)
