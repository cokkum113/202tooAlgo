import sys
input = sys.stdin.readline

nums = []

n, m = map(int, input().split())
xlist = list(map(int, input().split()))
xlist.sort()

visited = [False] * n

def backtracking(index):
    if len(nums) == m:
        print(*nums)
        return
    
    for i in range(n):
        if not visited[i]:
            if nums and nums[-1] < xlist[i] or len(nums) == 0:
                visited[i] = True
                nums.append(xlist[i])
                backtracking(index + 1)
                nums.pop()
                visited[i] = False

backtracking(0)
