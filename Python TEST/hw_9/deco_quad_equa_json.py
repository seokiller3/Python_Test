import json
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


def complex_encoder(obj):
    if isinstance(obj, complex):
        return {"real": obj.real, "imag": obj.imag}
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


def quadratic_solver_decorator(output_filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            data = {
                "input": args,
                "result": result
            }

            with open(output_filename, 'a') as file:
                json.dump(data, file, default=complex_encoder)
                file.write('\n')

            return result

        return wrapper

    return decorator


@quadratic_solver_decorator('results.json')
def solve_quadratic_with_logging(a, b, c):
    return solve_quadratic(a, b, c)


filename = 'random_numbers.csv'

with open('results.json', 'w') as file:
    pass  # Создаем или очищаем файл перед началом выполнения

with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) == 3:
            a, b, c = map(float, row)
            print(f"Коэффициенты: a={a}, b={b}, c={c}")
            roots = solve_quadratic_with_logging(a, b, c)
            print("Корни:", roots)
        else:
            print("Ошибка: требуются три числа в строке")
