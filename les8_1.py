class Data:
    t_m = ""

    def __init__(self, line):
        Data.t_m = line

    # @property
    @staticmethod
    def transform(m):
        data = [int(el) for el in m.split("-")]
        return data

    @classmethod
    def validate(cls, data):
        if data[0] <= 31 & data[0] >= 1:
            if data[1] <= 12 & data[1] >= 1:
                if data[2] <= 2009 & data[2] >= 1:
                    print(f"Дата введена корректно")
                else:
                    print(f"Не корректно введен год {data[2]}")
            else:
                print(f"Не корректно введен месяц {data[1]}")
        else:
            print(f"Не корректно введен день {data[0]}")


# q1 = input("Введите дату в формате число, месяц, год хх-хх-хх: ")
q1 = "01-02-2009"
t = Data(q1)
t_t = Data.transform(t.t_m)
Data.validate(t_t)
