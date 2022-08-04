import sys
input = sys.stdin.readline

n, m = map(int, input().split())
xlist = list(map(int, input().split()))
xlist.sort()

nums = []

def backtracking(index):
    if len(nums) == m:
        print(*nums)
        return
    
    x = 0
    
    for i in range(n):
        if x != xlist[i]:
            nums.append(xlist[i])
            x = xlist[i]
            backtracking(index + 1)
            nums.pop()
backtracking(0)