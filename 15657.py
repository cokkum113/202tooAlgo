import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = []

xlist = list(map(int, input().split()))
xlist.sort()

def backtracking(index):
    if len(nums) == m:
        print(*nums)
        return
    
    for i in range(n):
        if nums and nums[-1] <= xlist[i] or not nums:
            nums.append(xlist[i])
            backtracking(index + 1)
            nums.pop()

backtracking(0)
