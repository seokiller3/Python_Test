import math
import argparse
import logging

# Настройка логирования
logging.basicConfig(filename='quadratic_solver.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')


def solve_quadratic(a, b, c):
    """
    Решает квадратное уравнение вида ax^2 + bx + c = 0.

    Args:
        a (float): Коэффициент при x^2.
        b (float): Коэффициент при x.
        c (float): Свободный коэффициент.

    Returns:
        tuple or float or complex: Корни квадратного уравнения.
    """
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


def main():
    parser = argparse.ArgumentParser(description="Решение квадратного уравнения ax^2 + bx + c = 0")
    parser.add_argument('a', type=float, help="Коэффициент a")
    parser.add_argument('b', type=float, help="Коэффициент b")
    parser.add_argument('c', type=float, help="Коэффициент c")

    args = parser.parse_args()

    try:
        a = args.a
        b = args.b
        c = args.c

        logging.info(f"Решение квадратного уравнения: {a}x^2 + {b}x + {c} = 0")

        roots = solve_quadratic(a, b, c)

        if isinstance(roots, tuple):
            logging.info("Корни квадратного уравнения:", roots)
            print("Корни квадратного уравнения:", roots)
        else:
            logging.info("Корень квадратного уравнения:", roots)
            print("Корень квадратного уравнения:", roots)
    except ValueError:
        logging.error("Ошибка: Введите числовые значения коэффициентов a, b и c.")
        print("Ошибка: Введите числовые значения коэффициентов a, b и c.")
    except ZeroDivisionError:
        logging.error("Ошибка: Коэффициент a не может быть равен нулю.")
        print("Ошибка: Коэффициент a не может быть равен нулю.")


if __name__ == "__main__":
    main()
