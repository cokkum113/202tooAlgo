import sys
input = sys.stdin.readline

# 두개 , 한개로 나눠서 투포인터를 움직이면 될 거 같음

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

cnt = 0
for i in range(n):
    ans = nums[i]
    # 이 값과 투포인터의 합이 0이 되게 움직이면됨

    lo = i + 1
    hi = n - 1

    total = 0

    while lo < hi:
        total = nums[lo] + nums[hi]
        if total + ans == 0:
            cnt += 1
            
        if total < ans:
            total -= nums[lo]
            lo += 1
            total += nums[lo]
            
        elif total > ans:
            total -= nums[hi]
            hi -= 1
            total += nums[hi]
print(cnt)

