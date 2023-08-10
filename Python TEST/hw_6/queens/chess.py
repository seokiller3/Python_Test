from random import sample
from queens.check_queens import check_queens


def generate_queens(n):
    return sample(range(n), n)


if __name__ == '__main__':

    n = 8
    num_solutions = 4

    solutions_found = 0
    while solutions_found < num_solutions:
        coords = list(zip(generate_queens(n), generate_queens(n)))
        if check_queens(coords):
            print(coords)
            solutions_found += 1
