import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


dp = [[1001] * 3 for _ in range(n)]

dp[0][0] = graph[0][0]
dp[0][1] = graph[0][1]
dp[0][2] = graph[0][2]
for i in range(1, n):
    dp[i][0] = graph[i][0] + min(dp[i - 1][1] , dp[i - 1][2])
    dp[i][1] = graph[i][1] + min(dp[i - 1][0] , dp[i - 1][2])
    dp[i][2] = graph[i][2] + min(dp[i - 1][0] , dp[i - 1][1])
# print(dp)

print(min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))