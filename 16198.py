import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

maxi = 0

def backtracking(total):
    global maxi

    # 끝내는 부분
    if len(nums) == 2:
        maxi = max(maxi, total)
        return
    
    for i in range(1, len(nums) - 1):
        remember = total
        xx = nums[i - 1] * nums[i + 1]
        total += xx
        x = nums.pop(i)
        backtracking(total)
        nums.insert(i, x)
        total = remember

backtracking(0)
print(maxi)
