from random import randrange
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# ans = [1] * n
# 다이나믹프로그램으로 푸는 문제
dp = [1] * n
# 현재 위치까지 가장 증가된 큰값들 넣기

# 1, 4, 2, 3, 5
#cnt같은 값이 필요없음
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))