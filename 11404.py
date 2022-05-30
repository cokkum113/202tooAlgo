import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]


for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a][b] = min(cost, graph[a][b])
    # 같은 경로가 여러개 있을 수 있음!!!!


for i in range(n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1, n + 1):
    print(*graph[i][1:])
