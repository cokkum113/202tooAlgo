import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            break

        if i + graph[i][j] < n:
            dp[i + graph[i][j]][j] += dp[i][j]
        if j + graph[i][j] < n:
            dp[i][j + graph[i][j]] += dp[i][j]
print(dp[n - 1][n - 1])