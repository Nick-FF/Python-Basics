# -------------------6a----------------------#
from itertools import cycle
from itertools import count
p = int(input("Будет произведена генерация списка целых чисел. Введите число, с которого начинать "))
count_1 = 15


def iter(a, b):
    for i in count(a):
        if i > b:
            break
        else:
            print(i)


while True:
    iter(p, count_1)
    print(
        f"Сгенерировано {count_1 - p + 1} чисел. Для выхода нажмите q. для продолжения введите количество ")
    p = count_1 + 1
    count_1 = input()
    if count_1 == 'q':
        break
    else:
        count_1 = int(count_1) + p - 1
