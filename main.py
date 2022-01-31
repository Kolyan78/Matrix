import random


class Matrix:
    def __init__(self, new_matrix, column, string):
        self.list1 = new_matrix  # список, содержащий матрицу
        self.x = column  # размер матрицы по горизонтали
        self.y = string  # размер матрицы по вертикали
        self.list2 = None  # список ипользуется, когда нужна вторая матрица (сложение или умножение)
        self.list3 = None  # список содержащий итоговую матрицу (после сложения или умножения)
        self.num = None  # число, на которое умножается матрица в методе multiplication_num
        self.str_ = ""  # содержит строку сформированную для печати
        self.item = 0  # переменная для получения элемента матрицы при умножении
        self.string = []  # переменная для формирования строки матрицы при умножении

    def __repr__(self):
        """
        С помощью этого метода при сложении или умножении матриц, в виде аргумента методу можно передавать
        просто имя экземпляра, а не список.
        :return:
        """
        return f"{self.list1}"

    def add(self, second_matrix) -> list:
        """
        Метод складывает две матрицы
        :param second_matrix: вторая матрица, которая прибавляется к исходной
        :return: возвращает список, представляющий собой сумму двух матриц
        """
        self.list2 = second_matrix
        self.list3 = []
        for _ in range(self.y):
            self.list3.append([round(self.list1[_][j] + self.list2[_][j], 2) for j in range(x)])
        return self.list3

    def multiplication_num(self, number) -> list:
        """
        Метод умножает матрицу на число
        :param number: число, на которое будет умножена матрица
        :return: возвращает список, представляющий собой произведение матрицы на число num
        """
        self.num = number
        self.list3 = []
        for _ in range(self.y):
            self.list3.append([round(self.list1[_][j] * self.num, 2) for j in range(x)])
        return self.list3

    def print_matrix(self) -> str:
        """
        Метод печати матрицы. Используется для формирования строки для печати а не самой печати.
        То есть чтобы напечатать матрицу, надо написать следующее: print(m1.print_matrix()).
        :return: возвращает строку для печати матрицы с разделением на строки и выравниванием элементов по правому краю
        """
        self.str_ = ""
        for _ in range(y):
            for j in range(x):
                self.str_ += str("%.2f" % self.list1[_][j]).rjust(9)
            self.str_ += "\n"
        return self.str_

    def multiplication_matrices(self, list2):
        """
        Метод умножения двух матриц.
        :param list2: матрица, на которую надо умножить первую матрицу
        :return: возвращает список, представляющий собой произведение двух матриц
        """
        self.list2 = list2
        self.list3 = []
        self.string = []
        self.item = 0
        for _ in range(self.y):
            for j in range(self.x):
                for k in range(self.y):
                    self.item += (list_1[_][k] * list2[k][j])
                self.string.append(round(self.item, 2))
                self.item = 0
            self.list3.append(self.string)
            self.string = []
        return self.list3


"""
Матрицы создаются автоматически с рандомными значениями, размер матрицы тоже каждый раз рандомный.
Матрицы создаются только квадратные, так как умножать можно только квадратные матрицы
"""
x = y = random.randint(2, 10)
list_1 = []
list_2 = []

"""
Переменная num создается рандомно и используется для умножения матрицы на число
"""
num = round(random.uniform(-10, 10), 2)
for i in range(y):
    list_1.append([round(random.uniform(-10, 10), 2) for _ in range(x)])
    list_2.append([round(random.uniform(-10, 10), 2) for _ in range(x)])

"""
Создаем первую матрицу, используя список, размерностью x на y
Может быть проще будет при создании экземпляра класса давать просто список, а размерность матрицы
определялась бы внутри экземпляра? Вдруг пользователь задаст список одного размера, а размеры укажет другие?
Тогда будет или ошибка индекса если размеры будут больше, или посчитается только часть матрицы.
Например в методе __init__ добавить вычисление x и y.
"""
m1 = Matrix(list_1, x, y)

"""Создаем вторую матрицу"""
m2 = Matrix(list_2, x, y)

"""Выведем обе матрицы на экран используя метод print_matrix"""
print(f"Первая матрица ({m1.x}x{m2.y}):\n{m1.print_matrix()}")
print(f"Вторая матрица ({m2.x}x{m2.y}):\n{m2.print_matrix()}")

"""Создадим новый экземпляр класса, поместив в него результат метода add - сложение двух матриц"""
m3 = Matrix(m1.add(list_2), m1.x, m2.y)
print(f"Сложение двух матриц:\n{m3.print_matrix()}")

"""Создадим новый экземпляр класса, поместив в него результат метода multiplication_num - умножение матрицы на число"""
m4 = Matrix(m1.multiplication_num(num), m1.x, m1.y)
print(f"Умножение матрицы на {num}:\n{m4.print_matrix()}")

"""Создадим новый экземпляр класса, поместив в него результат метода multiplication_matrices - умножение двух матриц"""
m5 = Matrix(m1.multiplication_matrices(list_2), m1.x, m1.y)
print(f"Умножение двух матриц:\n{m5.print_matrix()}")
