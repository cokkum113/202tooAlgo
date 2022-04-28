import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(set(map(int, input().split())))

nums.sort()
ans = []

def backtracking(index):
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(len(nums)):
        if index == 0 or ans[-1] <= nums[i]:
            ans.append(nums[i])
            backtracking(index + 1)
            ans.pop()

backtracking(0)