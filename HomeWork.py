# a = int(input("Введите целое чило "))
# n = input("Как ваше имя ")

# ----------------------------------------------#
# ts = int(input("Введите время в секундах "))
# tm = int(ts / 60)
# if tm >= 59:
#     th = int(tm / 60)
#     tmin = int(tm - th * 60)
#     tsec = ts - (th * 60 * 60)
# else:
#     th = 0
#     tsec = ts - (tm * 60)
# if tm < 1:
#     tsec = ts
#     tmin = 0
#     th = 0
# format(th, '')
# print(f"Время в часах {th}:{tmin}:{tsec}")

# ---------------------------------------#

# a = int(input("Введите целое чило от 1 до 9"))
# a1 = a * 10 + a
# a2 = a * 100 + a1
# print(f"Результат {a + a1 +a2}")

# ---------------------------------------------#

a = int(input("Введите целое положительное чило"))
c = 0
while a != 0:
    b = a % 10
    if b > c:
        c = b
    a = a // 10

print(f"Самая большая цифра в этом числе {c}")
