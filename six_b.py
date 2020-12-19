# -------------------6b----------------------#
from itertools import cycle
count_1 = 15


def iter(a):
    c = 0
    for i in cycle("Yield"):
        if c >= a:
            break
        else:
            print(i)
            c += 1


while True:
    iter(count_1)
    print(
        f"Сгенерировано {count_1} повторений. Для выхода нажмите q. для продолжения введите количество ")
    count_1 = input()
    if count_1 == 'q':
        break
    else:
        count_1 = int(count_1)
