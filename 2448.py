import sys
input = sys.stdin.readline

n = int(input())
board = [[' '] * 2 * n for _ in range(n)]

def make_star(x, y, n):
    if n == 3:
        board[x][y] = '*'
        board[x + 1][y - 1] = '*'
        board[x + 1][y + 1] = '*'
        for k in range(-2, 3):
            board[x + 2][y + k] = '*'
    else:
        new_n = n//2
        make_star(x, y, new_n)
        make_star(x + new_n, y - new_n, new_n)
        make_star(x + new_n, y + new_n, new_n)
    return board


ans = make_star(0, n - 1, n)
for i in ans:
    print(''.join(i))