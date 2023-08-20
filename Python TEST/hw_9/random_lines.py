import csv
import random


def generate_random_numbers(min_value, max_value, num_numbers):
    return [random.randint(min_value, max_value) for _ in range(num_numbers)]


def generate_csv(filename, num_rows, num_numbers_per_row, min_value, max_value):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(num_rows):
            random_numbers = generate_random_numbers(min_value, max_value, num_numbers_per_row)
            writer.writerow(random_numbers)


num_rows = random.randint(100, 1000)  # Случайное число строк от 100 до 1000
num_numbers_per_row = 3  # Три случайных числа в каждой строке
min_value = 1  # Минимальное значение случайных чисел
max_value = 1000  # Максимальное значение случайных чисел
filename = 'random_numbers.csv'  # Имя файла

generate_csv(filename, num_rows, num_numbers_per_row, min_value, max_value)
print(f"Сгенерирован CSV файл '{filename}' с {num_rows} строками.")
