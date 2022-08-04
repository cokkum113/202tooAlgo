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
    
    for i in range(n):
        nums.append(xlist[i])
        backtracking(index + 1)
        nums.pop()

backtracking(0)
    
