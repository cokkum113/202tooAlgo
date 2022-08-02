import sys
input = sys.stdin.readline

# dp 에 올 수 있는 방향의 최대값을 넣어놓으면된다
# dp의 i,j의 현재위치를 나타내는 것이고 dp[i][j]는 그 위치까지의 최대값을 넣어놓는 것이다

n, m = map(int, input().split())
graph = [[0] * (m + 1)]

for _ in range(n):
    graph.append([0] + list(map(int, input().split())))


dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = graph[i][j] + max(dp[i - 1][j], dp[i][j - 1], dp[i -1][j - 1])
    

print(dp[-1][-1])