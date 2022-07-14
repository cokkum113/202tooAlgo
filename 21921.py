import sys
input = sys.stdin.readline

n, x = map(int, input().split())

nums = list(map(int, input().split()))
anslist = []

lo = 0
hi = x - 1
# hi를 0으로도 해보고, 1로도 해봤으나, 처음부터 hi를 계산해야하는 범위로 설정하고
# lo 값을 움직이면됨

maxi = 0
total = sum(nums[:x])
anslist.append(total)

# 우선 인덱스를 움직이면서 x명이 되면 계산하고 제일 앞에있는 수를 pop하고, 
# 또 하나 더 추가해서 넣고, deque로 이런식으로 생각했으나
# 인덱스를 사용하니까 이방법이 필요가 없음. 
# xxx = 0
# cnt = 0 cnt도 필요 없음

while True:
    # if xxx == 4:
    #     break

    if hi == n - 1:
        break

    # 인덱스를 여기서 움직이면될거같음
    total -= nums[lo]
    lo += 1
    hi += 1
    total += nums[hi]

    anslist.append(total)
    
maxi = max(anslist)

if maxi == 0:
    print('SAD')
else:
    print(maxi)
    print(anslist.count(maxi))