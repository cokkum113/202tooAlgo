import sys
input = sys.stdin.readline

n, c = map(int, input().split())
nums = [int(input()) for _ in range(n)]

nums.sort()

# 둘 사이의 최소 간격 : x
# 이 최소간격으로 둘 수 있는 공유기 갯수 : y

# 간격들이 움직일 값, 파라미터
lo = 1
hi = nums[-1] - nums[0]

ans = 0
# 내가 구하는 최소 x값의 최대값.

while True:
    if lo > hi:
        break

    cnt = 1 # 항상 하나는 두고 시작해야함
    # if lo == hi:
    #     break
    mid = (lo + hi) // 2
    now_pos = nums[0]
    # x의 최소값을 구하는 방법
    mini_x = int(1e9)
    now = 0
    for i in range(1, n):
        # 공유기를 둘 수 있을 때,
        if mid <= nums[i] - now_pos:
        # 간격보다 크다면 공유기를 그 사이에 둘 수 있고, 두게 되면 x값은 줄어들거나 안줄어들 수 있다.
            now = nums[i] - now_pos
            mini_x = min(mini_x, now)
            cnt += 1
            now_pos = nums[i]
    # 이제 mini x를 가지고 mini x가 최대값일 때를 구하면됨

    if cnt >= c:
        #이때 답이 나올 수 있음 근데 이때 x 값도 달라질수 있음
        # 왜냐면 답이 나올 수 있는데 감소그래프에서 x축으로 쪼금만 가도 답이 또 나올 수 있기 때문에
        # 이떄 최대값을 구해주면됨
        ans = max(ans, mini_x)

        # cnt 값이 더 많다는 것은 두개 사이의 넓혀서 
        # y값인 둘 수 있는 것을 줄여야한다는 것
        # 따라서 
        lo = mid + 1
    elif cnt < c:
        # 카운트된 값이 적다는 것은 
        # 답이 아니라는 뜻 즉, 답이 나올 수가 없음 무조건 하나를 더 추가해야함

        # 또한, 간격을 좁혀서 더 많이 둬야함
        hi = mid - 1

print(ans)