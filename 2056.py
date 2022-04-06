import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
jobs = [[] for _ in range(n + 1)]

time = [0] * (n + 1)
indegree = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1):
    l = list(map(int, input().split()))
    time[i] = l[0]

    if l[1] != 0:
        for j in range(2, len(l)):
            jobs[l[j]].append(i)
            indegree[i] += 1

que = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        que.append(i)
        dp[i] = time[i]

while que:
    now = que.popleft()
    for i in jobs[now]:
        indegree[i] -= 1
        dp[i] = max(dp[now] + time[i], dp[i])
    
        if indegree[i] == 0:
            que.append(i)

print(max(dp))