import sys
input = sys.stdin.readline

n = int(input())

board = [0] * n
ans = 0

def check(st):
    for i in range(st):
        if abs(board[st] - board[i]) == st - i: 
            # 열 - 열 == 행 - 행 : 대각선
            return False
    return True

def backtracking(st):
    global ans
    if st == n:
        ans += 1
        return
    
    for i in range(n): # i는 다 돌면서 0~전까지 옮겨가면서 유망한 곳 찾는것
        board[st] = i
        if check(st):
            backtracking(st + 1)

backtracking(0)
print(ans)
        