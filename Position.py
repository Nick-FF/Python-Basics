from Worker import Worker


class Position(Worker):
    def get_full_name(self, n, s):
        name = n
        surname = s
        print(name + " " + surname)

    def get_total_income(self, w, b):
        self.wage = w
        self.bonus = b
        print(f"Доход {self.wage + self.bonus}")


work = Position()
name = "Степан"
surname = "Аркадьевич"
__income = 100, 40
print(work.get_full_name(name, surname))
print(work.get_total_income(*__income))
