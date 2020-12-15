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

# a = int(input("Введите целое положительное чило"))
# c = 0
# while a != 0:
#     b = a % 10
#     if b > c:
#         c = b
#     a = a // 10

# print(f"Самая большая цифра в этом числе {c}")
# -------------------5----------------------#

#-----------------Lesson2-------------------#
# -------------------1----------------------#
# list_1 = [1, 'a', [1, 3], 3.1, None]
# list_2 = []
# for i in list_1:
#     list_2.append(type(i))
#     print(type(i))
# print(list_2)

# -------------------2:2----------------------#

# -------------------2:3----------------------#

# q = {
#     1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август", 9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"
# }
# corr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# month = int(input("Ведите число от 1 до 12 "))

# print(f"Вы выбрали месяц {q[month]}") if month in corr else print(
#     f"Вы ввели некорректное значение")
# -------------------2:6----------------------#
# заполните информацио о товарах (запрос данных)
# создание цикла опроса с возрастающей нумерацией (до 4 например), задавать запросы
# в цикле заполнять словарь, сохранить все в заранее подготовленном списке и созранить в кортеж
# qwes1 = int(
#     input("Заполните информацию о товаре. Сколько товаров вы хотите внести? "))
# dic = {"название": 1, "цена": 2, "количество": 3, "ед.": 4}
# list_b = []
# list_tuple = []
# i = 0
# while i < qwes1:
#     list_b.clear()
#     print(f"Товар {i + 1}")
#     list_b.append(i + 1)
#     qwes2 = input("Название товара ")
#     qwes3 = input("Цена товара ")
#     qwes4 = input("Количество товара ")
#     qwes5 = input("Единицы измерения товара ")
#     dic.update({"название": qwes2, "цена": qwes3,
#                 "количество": qwes4, "ед.": qwes5})
#     list_b.append(dic.copy())
#     list_tuple.append(tuple(list_b))
#     print("Результат ", list_tuple[i])
#     i += 1
# print("Результат ")
# for j in range(len(list_tuple)):
#     print(list_tuple[j])

#-----------------Lesson3-------------------#
# -------------------1----------------------#
# print("Деление: первое число/второе число")
# qw1 = int(input("Введите первое число "))
# qw2 = int(input("Введите второе число "))


# def div(a, b):
#     c = a / b if b != 0 else print("На ноль делить нельзя")
#     print(c)


# div(qw1, qw2)

# -------------------2----------------------#
# q1 = input("Введите через запятую: имя, фамилия, год рождения, город проживания, email, телефон ").split(', ')
# # print(q1)


# def data_preson(name, s_name, b_year, city, email, phone_numb):
#     print(name, s_name, b_year, city, email, phone_numb)


# data_preson(name=q1[0], s_name=q1[1], b_year=q1[2],
#             city=q1[3], email=q1[4], phone_numb=q1[5])

# -------------------3----------------------#
# print("Введите три числа ")
# n1 = int(input(
#     "число 1="))
# n2 = int(input(
#     "число 2="))
# n3 = int(input(
#     "число 3="))


# def my_func(a, b, c):
#     d = [(a + b), (b + c), (c + a)]
#     print(max(d))


# my_func(n1, n2, n3)
# -------------------4----------------------#
print("Введите действительное число-основание и отрицательное целое число-степень ")
n1 = float(input(
    "число 1="))
n2 = int(input(
    "число 2="))


def pow_1(a, b):
    c = a ** b
    print(c)


def pow_2(a, b):
    d = b * -1
    e = a
    i = 1
    while i < d:
        e = e * a
        i += 1
        print(e)
    c = 1 / e
    print(c)


pow_1(n1, n2)
pow_2(n1, n2)
# -------------------5----------------------#

# def data_sum(args):
#     global total
#     sum = 0
#     i = 0
#     while i < (len(args)):
#         # for i in args:
#         sum = sum + int(args[i])
#         i += 1
#     total = total + sum
#     print(f"{total} ({sum})")


# q1 = input("Введите числа через пробел, для завершения нажать q: ").split(' ')
# print(q1)
# condition = True
# total = 0
# while condition == True:
#     q1 = input().split(' ')
#     print(q1)
#     data_sum(q1)
#     if (q1.count(q) != 0):
#         break
