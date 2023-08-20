import csv
import math


def solve_quadratic(a, b, c):
    # Вычисление дискриминанта
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        # Два действительных корня
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        # Один действительный корень
        root = -b / (2 * a)
        return root
    else:
        # Корни комплексные
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2


def quadratic_solver_decorator(func):
    def wrapper(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    a, b, c = map(float, row)
                    print(f"Коэффициенты: a={a}, b={b}, c={c}")
                    roots = func(a, b, c)
                    print("Корни:", roots)
                else:
                    print("Ошибка: требуются три числа в строке")

    return wrapper


@quadratic_solver_decorator
def solve_quadratic_from_csv(a, b, c):
    return solve_quadratic(a, b, c)


filename = 'random_numbers.csv'
solve_quadratic_from_csv(filename)
