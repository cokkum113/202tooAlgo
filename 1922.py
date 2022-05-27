import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

heap = []

visited = [False] * (n + 1)
start = 1
visited[start] = True

for e in graph[start]:
    heapq.heappush(heap, e)

cnt = 0
ans = 0
while cnt < n - 1:
    cost, v = heapq.heappop(heap)
    if visited[v]:
        continue
    else:
        cnt += 1
        visited[v] = True
        ans += cost
        for next in graph[v]:
            heapq.heappush(heap, next)


print(ans)

