# homework 7
# task 1
print("Task 1")
print()

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    @property
    def matrix(self):
        return self.__matrix

    @matrix.setter
    def matrix(self, matrix):
        if isinstance(matrix, list) and all(isinstance(elem, list) for elem in matrix):
            length = len(matrix[0])
            t = type(matrix[0][0])
            for i in range(1, len(matrix)):
                if length != len(matrix[i]):
                    raise ValueError("Передана не прямоугольная таблица")
                for el in matrix[i]:
                    if t != type(el):
                        raise ValueError("Все типы матрицы должны быть одинаковыми")
            self.__matrix = matrix
        else:
            raise ValueError("Передан не список списков")

    def __str__(self):
        m = ""
        for row in self.matrix:
            s = ""
            for cell in row:
                s += " " + str(cell)
            m += "\n" + s[1:]
        return m[1:]

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise TypeError("Разный размер матриц")
        else:
            result = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[i])):
                    row.append(self.matrix[i][j] + other.matrix[i][j])
                result.append(row)
        return Matrix(result)

m1 = Matrix([[11, 12], [21, 22], [31, 32]])
m2 = Matrix([[23, 13], [22, 12], [21, 11]])
m3 = m1 + m2
print(m1)
print("-----")
print(m2)
print("-----")
print(m3)

# task 2
print()
print("Task 2")
print()

from abc import ABC, abstractmethod

class Clothes(ABC):
    @property
    @abstractmethod
    def p(self):
        pass

    @p.setter
    @abstractmethod
    def p(self, p):
        pass

    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    @property
    def p(self):
        return self.__p

    @p.setter
    def p(self, p):
        try:
            self.__p = float(p)
        except ValueError:
            print("Не число")
            self.__p = 0

    def __init__(self, p):
        self.p = p

    def consumption(self):
        return self.p / 6.5 + 0.5

class Suit(Clothes):
    @property
    def p(self):
        return self.__p

    @p.setter
    def p(self, p):
        try:
            self.__p = float(p)
        except ValueError:
            print("Не число")
            self.__p = 0

    def __init__(self, p):
        self.p = p

    def consumption(self):
        return 2 * self.p + 0.3

c = Coat(48)
s = Suit(1.82)
print(c.consumption())
print(s.consumption())

# task 3
print()
print("Task 3")
print()

class Cell:
    def __init__(self, count):
        self.__count = count

    def __add__(self, other):
        return Cell(self.__count + other.__count)

    def __sub__(self, other):
        if self.__count < other.__count:
            raise Exception("Вычитаем из меньшего")

        return Cell(self.__count - other.__count)

    def __mul__(self, other):
        return Cell(self.__count * other.__count)

    def __truediv__(self, other):
        return Cell(self.__count // other.__count)

    def __str__(self):
        return f"Cell = {self.__count}"

    def make_order(self, n):
        s = ""

        for i in range(self.__count // n):
            s += ("*" * n) + "\\n"

        n = self.__count - n * (self.__count // n)

        if n > 0:
            s += ("*" * n)
        else:
            s = s[:-2]

        return s


c1 = Cell(5)
c2 = Cell(3)
print(c1)
print(c2)
print(c1 + c2)
print(c1 - c2)
try:
    print(c2 - c1)
except Exception as e:
    print(f"Ошибка {e}")
print(c1 * c2)
print(c1 / c2)
print(c1.make_order(3))
print(c2.make_order(5))
print(Cell.make_order(Cell(8), 3))