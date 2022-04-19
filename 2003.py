import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))

lo = 0
hi = 0

ans = nums[0]

cnt = 0
while True:
    if hi == n - 1 and ans < m:
        break

    if ans < m:
        hi += 1
        ans += nums[hi]
    
    elif ans > m:
        ans -= nums[lo]
        lo += 1
    
    elif ans == m:
        ans -= nums[lo]
        cnt += 1
        lo += 1

print(cnt)
    

