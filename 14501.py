import sys
input = sys.stdin.readline

n = int(input())
date = [0]
pay = [0]

for _ in range(n):
    x, y = map(int, input().split())
    date.append(x)
    pay.append(y)


dp = [0] * (n + 2)

for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], dp[i])
    if i + date[i] <= n + 1:
        dp[i + date[i]] = max(dp[i + date[i]], dp[i] + pay[i])

print(max(dp))