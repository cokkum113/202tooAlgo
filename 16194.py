import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums = [0] + nums
dp = [10001] * (n + 1)

dp[1] = nums[1]
for i in range(1, n + 1):
    for j in range(1, i):
        dp[i] = min(dp[i], dp[i - j] + nums[j], nums[i])
print(dp[n])