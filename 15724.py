import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] for _ in range(n + 1)]
for i in range(n):
    x = list(map(int, input().split()))
    for j in x:
        graph[i + 1].append(j)
# print(graph)

k = int(input())
# sx, sy, ex, ey
# 어떻게 dp의 파라미터로 사용할 것인지
# dp는 어떻게 무슨 합이 dp의 값이 될것이고 dp의 파라미터는 무엇이 될 것인지
# dp의 누적합 규칙을 찾음!!!
# dp[1][1] = dp[0][1] + dp[1][0] - dp[0][0] + graph[1][1]

dp = [[0] * (m + 1) for _ in range(n + 1)]

# dp[0][0] = graph[0][0]

# dp[0] = graph[0]
# 이 방법일 때문에 역시, 양 사이드에 0을 더 채워주는 방식으로하면 해결이 가능하다!!!!!!!!!!!1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + graph[i][j]
# print(dp)
for t in range(k):
    sx, sy, ex, ey = map(int, input().split())
    print(dp[ex][ey] - dp[sx - 1][ey] - dp[ex][sy - 1] + dp[sx - 1][sy - 1])
    