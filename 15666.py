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
        if nums and nums[-1] <= xlist[i] or len(nums) == 0:
            if x != xlist[i]:
                x = xlist[i]
                nums.append(xlist[i])
                backtracking(index + 1)
                nums.pop()
backtracking(0)