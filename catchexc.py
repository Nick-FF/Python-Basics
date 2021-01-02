class CatchError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def ValueErr(self, exc):
        print(exc)


# print("Давайте что-нибудь разделим")
# inp_data_1 = input("Введите делимое. Должно быть не отрицательным: ")
# inp_data = input("Введите делитель: ")

# try:
#     inp_data = int(inp_data)
#     inp_data_1 = int(inp_data_1)
#     if inp_data == 0:
#         raise CatchError("Деление на ноль!")
#     if inp_data_1 < 0:
#         raise CatchError("Вы ввели отрицательное число!")

# except CatchError as err:
#     print(err)
# except ValueError:
#     print("Вы ввели не число")
# else:
#     print(f"Все хорошо. Ваше число: {inp_data}")


print("Заполните список. Вводите числа. Если закончили введите stop")
try:
    i = 0
    a = []
    while True:
        inp_data = input(f"Введите {i+1} число: ")
        if inp_data == "stop":
            raise CatchError("Ввод данных остановлен")
        try:
            inp_data = int(inp_data)
            a.append(inp_data)
            i += 1
        except ValueError as alarm:
            print("Fatal error. Введите число!")
        # raise CatchError(str(alarm))
        # except CatchError as err:
        #     print(err)
except CatchError as err:
    print(err)
finally:
    print(a)
