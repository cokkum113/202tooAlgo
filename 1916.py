import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())
INF = int(1e9)

heap = []

visited = [False] * (n + 1)
dis = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y, cost = map(int, input().split())
    graph[x].append([cost, y])

st, end = map(int, input().split())

heapq.heappush(heap, [0, st])
dis[st] = 0

while heap:
    T = heapq.heappop(heap)
    current = T[1]

    if visited[current]:
        continue
    else:
        visited[current] = True

        for next in graph[current]:
            if dis[next[1]] > dis[current] + next[0]:
                dis[next[1]] = dis[current] + next[0]
                heapq.heappush(heap, [dis[next[1]], next[1]])

print(dis[end])
