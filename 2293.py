import sys
input = sys.stdin.readline

n, k = map(int, input().split())

nums = []
for _ in range(n):
    nums.append(int(input()))

dp = [0] * (k + 1)

dp[0] = 1

for i in nums:
    for j in range(1, k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]
print(dp[-1])