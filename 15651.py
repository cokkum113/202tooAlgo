import sys
input = sys.stdin.readline

n, m = map(int, input().split())


nums = []

def bactracking(index):
    if len(nums) == m:
        print(*nums)
        return
    
    for i in range(1, n + 1):
        nums.append(i)
        bactracking(index + 1)
        nums.pop()
    
bactracking(0)