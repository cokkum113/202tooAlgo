import sys
input = sys.stdin.readline

day = [0]
val = [0]
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    day.append(x)
    val.append(y)

dp = [0] * (n + 2)

# dp[1] = 0
# dp[2] = 0
# dp[3] = 0
# dp[4] = 10

# dp[2] = 0
# dp[3] = 0
# dp[4] = 0
# dp[5] = 0
# dp[6] = 0
# dp[7] = 20

# dp[1] = 0
# dp[2] = 0
# dp[3] = 0
# dp[4] = 10

# dp[1] = 0
# dp[2] = 0
# dp[3] = 0
# dp[4] = 0
# dp[5] = 20

for i in range(1, n + 1):
    if i + day[i] <= n + 1:
        dp[i] = max(val[i + day[i]], dp[i] + val[i])

print(dp)
