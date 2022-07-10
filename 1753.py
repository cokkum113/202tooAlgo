import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)
v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)
distance = [INF] * (v + 1)

k = int(input())

for _ in range(e):
    st, end, cost = map(int, input().split())
    graph[st].append([cost, end])

heap = []
heapq.heappush(heap,[0, k])
distance[k] = 0

while heap:
    T = heapq.heappop(heap)
    current = T[1]

    if visited[current]:
        continue
    else:
        visited[current] = True
    
    for next in graph[current]:
        if distance[next[1]] >= distance[current] + next[0]:
            distance[next[1]] = distance[current] + next[0]
            heapq.heappush(heap, [distance[next[1]], next[1]])

for i in range(1, v + 1):
    if distance[i] == int(1e9):
        print('INF')
    else:
        print(distance[i])
