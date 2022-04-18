import sys
input = sys.stdin.readline

n = int(input())
pack = list(map(int, input().split()))
pack = [0] + pack
dp = [0] * (n + 1)

dp[1] = pack[1]
for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], pack[j] + dp[i - j])

print(dp[n])
