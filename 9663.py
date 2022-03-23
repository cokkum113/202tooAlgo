import sys
input = sys.stdin.readline

n = int(input())

visit = [False] * n
board = [0] * n
ans = 0

def check(st):
    for i in range(st):
        if abs(board[st] - board[i]) == st - i:
            return False
    return True

def backtracking(st):
    global ans
    if st == n:
        ans += 1
        return
    
    for i in range(n):
        if visit[i] == True:
            continue

        board[st] = i
        if check(st):
            visit[i] = True
            backtracking(st + 1)
            visit[i] = False

backtracking(0)
print(ans)
        