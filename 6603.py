import sys
input = sys.stdin.readline

def backtracking(index):
    if len(nums) == 6:
        print(*nums)
        return
    
    for i in range(n):
        if visited[i] == False:
            nums.append(xx[i])
            visited[i] = True
            backtracking(index + 1)
            visited[i] = False
            nums.pop()

while True:
    x = list(map(int, input().split()))
    n = x[0]
    nums = []

    visited = [False] * n
    if n == 0:
        break
    else:
        xx = x[1:]
        backtracking(0)

