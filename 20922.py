from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
anslist = deque()
# 답들을 넣을 리스트, 이것의 Len값을 구하면됨.
numbers = list(map(int, input().split()))
lo = 0
hi = 0
# 투포인터

maxi = 0
cnt = [0] * (100001)

while True:
    if hi == n:
        break

    if cnt[numbers[hi]] < k:
        cnt[numbers[hi]] += 1
        anslist.append(numbers[hi])
        hi += 1

    else:
        cnt[numbers[lo]] -= 1
        lo += 1
        
        if anslist:
            anslist.popleft()
    maxi = max(maxi, len(anslist))
print(maxi)
            

        
