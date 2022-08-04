import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = []

def backtracking(index):
    if len(nums) == m:
        print(*nums)
        return
    
    for i in range(1, n + 1):
        if nums and nums[-1] <= i or not nums:
            nums.append(i)
            backtracking(index + 1)
            nums.pop()

backtracking(0)