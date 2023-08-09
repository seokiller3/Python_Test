from queens.check_queens import check_queens

if __name__ == '__main__':
    coords = [(0, 0), (1, 4), (2, 7), (3, 5), (4, 2), (5, 6), (6, 1), (7, 3)]
    print(check_queens(coords))
