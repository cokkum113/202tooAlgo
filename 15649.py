import sys
input = sys.stdin.readline

n, m = map(int, input().split())

visited = [False] * (n + 1)
nums = []


def backtracking(index):
    if len(nums) == m:
        print(*nums)
        return
    
    for i in range(1, n + 1):
        if visited[i] == False:
            nums.append(i)
            visited[i] = True
            backtracking(index + 1)
            visited[i] = False
            nums.pop()

backtracking(0)
