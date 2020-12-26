class Matrix:

    def __init__(self, argv):
        self.arg = argv
        self.result = []

    def print_matrix(self, out, matrix):
        print(out)
        for i in matrix:
            print(i)
        print('')

    def __str__(self):
        for i in (('Первая матрица', a.arg), ('Вторая матрица', b.arg), ('Результирущая матрица', c.arg)):
            self.print_matrix(i[0], i[1])
        # return self.print_matrix("i[0]", a + b)
        return f"Объект с параметрами ({c.arg})"

    def __add__(self, other):

        for sublist in zip(self.arg, other.arg):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
                temp.append(sum(numbers))
            self.result.append(temp)
        return self.result


matrix1 = [[1, 2, 3], [4, 5, 6], [2, 4, 6]]
matrix2 = [[1, 2, 3], [4, 5, 6], [2, 4, 6]]

a = Matrix(matrix1)
b = Matrix(matrix2)
d = a + b
c = Matrix(d)
# print(a + b)
print(c)
