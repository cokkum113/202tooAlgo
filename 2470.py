import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.sort()

lo = 0
hi = n - 1
mini = int(1e9)

xx = nums[lo] + nums[hi]
ans = []
while lo < hi:

    if mini > abs(xx):
        mini = abs(xx)
        ans = [nums[lo], nums[hi]]
    
    if xx == 0:
        ans = [nums[lo], nums[hi]]
        break
    elif xx > 0:
        xx -= nums[hi]
        hi -= 1
        xx += nums[hi]
    
    elif xx < 0:
        xx -= nums[lo]
        lo += 1
        xx += nums[lo]

print(*ans)
