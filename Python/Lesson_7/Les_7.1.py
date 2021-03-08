class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        gen = []
        for sub in zip(self.matrix, other.matrix):
            temp = []
            for numbers in zip(sub[0], sub[1]):
                temp.append(sum(numbers))
            gen.append(temp)
        return Matrix(gen)

    def __str__(self):
        return str(self.matrix)


matr_1 = [[1, 3], [8, 9]]
matr_2 = [[3, 2], [1, 9]]
matrix_1 = Matrix(matr_1)
matrix_2 = Matrix(matr_2)
print(f'Результат сложения 2-х матриц является новая матрица: {matrix_1 + matrix_2}')
