import sys
input = sys.stdin.readline

n, k = map(int, input().split())

goods = [[-1, -1]]
for _ in range(n):
    w, v = map(int, input().split())
    goods.append([w, v])

# goods.sort(key = lambda x : (x[1], x[0]),reverse= True)

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = goods[i][0]
        value = goods[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i- 1][j - weight] + value)

print(dp[n][k])