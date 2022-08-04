import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = []

xlist = list(map(int, input().split()))
xlist.sort()
visited = [False] * n

def backtracking(index):
    if len(nums) == m:
        print(*nums)
        return 
    
    x = 0
    for i in range(len(xlist)):
        if visited[i] == False and x != xlist[i]:
            visited[i] = True
            nums.append(xlist[i])
            x = xlist[i]
            backtracking(index + 1)
            nums.pop()
            visited[i] = False
    
print(backtracking(0))