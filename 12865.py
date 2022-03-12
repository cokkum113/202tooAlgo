import sys
input = sys.stdin.readline

n, k = map(int, input().split())

goods = [[-1, -1]]

for _ in range(n):
    w, v = map(int, input().split())
    goods.append([w, v])


dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        #j = 무게 
        weight = goods[i][0]
        value = goods[i][1]

        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])

# 13, 8, 6, 5
# ### 0   1  2  3 4  5  6  7
# 0  [[0, 0, 0, 0, 0, 0, 0, 0], 
# 1  [0, 0, 0, 0, 0, 0, 13, 13],
# 2  [0, 0, 0, 0, 8, 8, 13, 13],
# 3  [0, 0, 0, 6, 8, 8, 13, 14], 
# 4  [0, 0, 0, 6, 8, 12, 13, 14]]