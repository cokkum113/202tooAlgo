import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

lo = 0
hi = 0

total = nums[hi]
cnt = 0

while True:
    if hi == n - 1 and lo > hi:
        break

    if total == m:
        cnt += 1
        total -= nums[lo]
        lo += 1
        
    elif total > m:
        total -= nums[lo]
        lo += 1
        
    elif total < m:
        if hi == n - 1:
            total -= nums[lo]
            lo += 1
        elif hi < n - 1:
            hi += 1
            total += nums[hi]

print(cnt)