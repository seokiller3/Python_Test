class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def fill(self, values):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = values[i][j]

    def print(self):
        for row in self.data:
            print(" ".join(map(str, row)))

    def __eq__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матрицы должны быть одинаковыми для сложения")

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError(
                "Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                result.data[i][j] = total
        return result


# Пример использования класса Matrix

matrix1 = Matrix(2, 3)
matrix1.fill([[1, 2, 3], [4, 5, 6]])

matrix2 = Matrix(2, 3)
matrix2.fill([[7, 8, 9], [10, 11, 12]])

matrix3 = Matrix(3, 2)
matrix3.fill([[1, 2], [3, 4], [5, 6]])

print("Matrix 1:")
matrix1.print()

print("Matrix 2:")
matrix2.print()

print("Matrix 3:")
matrix3.print()

# Сравнение
print("Matrix 1 == Matrix 2:", matrix1 == matrix2)

# Сложение
matrix_sum = matrix1 + matrix2
print("Matrix Sum:")
matrix_sum.print()

# Умножение
matrix_product = matrix1 * matrix3
print("Matrix Product:")
matrix_product.print()
