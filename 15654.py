import sys
input = sys.stdin.readline

n, m = map(int, input().split())

xlist = list(map(int, input().split()))
xlist.sort()
visited = [False] * n
nums = []

def backtracking(index):
    if len(nums) == m:
        print(*nums)
        return
    
    for i in range(n):
        if visited[i] == False:
            nums.append(xlist[i])
            visited[i] = True
            backtracking(index + 1)
            visited[i] = False
            nums.pop()

backtracking(0)