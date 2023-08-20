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


# Пример использования
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

roots = solve_quadratic(a, b, c)

if isinstance(roots, tuple):
    print("Корни квадратного уравнения:", roots)
else:
    print("Корень квадратного уравнения:", roots)
