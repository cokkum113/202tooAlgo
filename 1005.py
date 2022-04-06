import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    builds = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    dp = [0] * (n + 1)
    time = [0]

    l = list(map(int, input().split()))
    time += l
    
    for i in range(k):
        x, y = map(int, input().split())
        indegree[y] += 1
        builds[x].append(y)
    
    w = int(input())
    
    que = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            que.append(i)
            dp[i] = time[i]
    
    while que:
        now = que.popleft()
        for i in builds[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now] + time[i], dp[i])
            if indegree[i] == 0:
                que.append(i)
            
    print(dp[w])

