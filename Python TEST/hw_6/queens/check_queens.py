def check_queens(coords):
    n = len(coords)
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        x, y = coords[i]
        if board[x][y] == 1:
            return False
        board[x][y] = 1
        for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
            for j in range(1, n):
                if 0 <= x + dx * j < n and 0 <= y + dy * j < n:
                    if board[x + dx * j][y + dy * j] == 1:
                        return False
    return True
