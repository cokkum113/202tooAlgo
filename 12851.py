import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

visited = [[-1, 0] for _ in range(100001)]

def bfs(st):
    q = deque()
    q.append(st)
    visited[st][0] = 0
    visited[st][1] = 1

    while q:
        pos = q.popleft()
        for i in [pos + 1, pos -1, pos * 2]:
            if 0 <= i < 100001:
                if visited[i][0] == -1:
                    visited[i][0] = visited[pos][0] + 1
                    visited[i][1] = visited[pos][1]
                    q.append(i)
                
                elif visited[i][0] == visited[pos][0] + 1:
                    visited[i][1] += visited[pos][1]
                
bfs(n)
print(visited[k][0])
print(visited[k][1])

