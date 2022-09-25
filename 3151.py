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
            # print(nums[i], nums[lo],nums[hi])
            cnt += 1
            lo += 1
            # hi -= 1 은 안됨.... -> 방향떄문에??둘이 같아 버렸다는 거니까 방향이 있는 거니까??!!

        if total + ans < 0:
            lo += 1

        elif total + ans > 0:
            hi -= 1
            
print(cnt)
# print(nums)
# [-6, -5, -4, -4, 0, 1, 2, 2, 3, 7]