from sys import argv
# script_name, work_hour, money_per_hour, bonus = argv


def calc(a):
    c = int(a[1]) * int(a[2]) + int(a[3])
    print(c)


calc(argv)
