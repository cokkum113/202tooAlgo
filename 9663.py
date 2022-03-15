import sys
input = sys.stdin.readline

n = int(input())

visited = [False] * n
board = [0] * n
ans = 0

def check(st):
    for i in range(st):
        if abs(board[st] - board[i]) == st - i: #대각선 가로세로의 차가 같다는 건 대각선이라는 뜻
            return False
    return True
    

def n_queen(st):
    global ans
    if st == n:
        ans += 1
        return
    
    for i in range(n):
        if visited[i]:
            continue

        board[st] = i

        if check(st):
            visited[i] = True
            n_queen(st + 1)
            visited[i] = False

n_queen(0)
print(ans)