# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы. Следующий шаг — реализовать
# перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f'{self.matrix[0][0]:>5}{self.matrix[0][1]:>5}{self.matrix[0][2]:>5}\n' \
               f'{self.matrix[1][0]:>5}{self.matrix[1][1]:>5}{self.matrix[1][2]:>5}\n' \
               f'{self.matrix[2][0]:>5}{self.matrix[2][1]:>5}{self.matrix[2][2]:>5}\n'

    def __add__(self, other):
        return Matrix([
            [self.matrix[0][0] + other.matrix[0][0], self.matrix[0][1] + other.matrix[0][1], self.matrix[0][2] + other.matrix[0][2]],
            [self.matrix[1][0] + other.matrix[1][0], self.matrix[1][1] + other.matrix[1][1], self.matrix[1][2] + other.matrix[1][2]],
            [self.matrix[2][0] + other.matrix[2][0], self.matrix[2][1] + other.matrix[2][1], self.matrix[2][2] + other.matrix[2][2]]
        ])


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_1)
print('***' * 10)
matrix_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_1 + matrix_2)
