import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

ans = nums[-1]
numbers = nums[:-1]

dp = [[0] * 21 for _ in range(n - 1)]
dp[0][numbers[0]] = 1

for i in range(1, n - 1):
    for j in range(21):
        if dp[i - 1][j] != 0:
            pre_val = j
            next_val = numbers[i]

            if 0 <= pre_val + next_val <= 20:
                dp[i][pre_val + next_val] += dp[i - 1][pre_val]
            if 0 <= pre_val - next_val <= 20:
                dp[i][pre_val - next_val] += dp[i - 1][pre_val]

print(dp[n - 2][ans])