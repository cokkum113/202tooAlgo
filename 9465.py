import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0] * n for _ in range(2)]

    graph = []
    for _ in range(2):
        graph.append(list(map(int, input().split())))

    dp[0][0] = graph[0][0]
    dp[1][0] = graph[1][0]

    dp[0][1] = graph[0][1] + dp[1][0]
    dp[1][1] = graph[1][1] + dp[0][0]

    for i in range(2, n):
        dp[0][i] = graph[0][i] + max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = graph[1][i] + max(dp[0][i - 1], dp[0][i - 2])
    
    print(max(dp[0][n - 1],dp[1][n - 1]))