from cmath import cos
import sys
input = sys.stdin.readline
import heapq

n, e = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])


v1, v2 = map(int, input().split())


def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(q, [0, start])
    while q:
        w, pos = heapq.heappop(q)
        if distance[pos] < w:
            continue

        for next_w , next_pos in graph[pos]:
            if distance[next_pos] > next_w + w:
                distance[next_pos] = next_w + w
                heapq.heappush(q, [distance[next_pos], next_pos])
    return distance




start_dijkstra = dijkstra(1)
v1_dijkstra = dijkstra(v1)
v2_dijkstra = dijkstra(v2)

ans = min(start_dijkstra[v1] + v1_dijkstra[v2] + v2_dijkstra[n] , start_dijkstra[v2]+ v2_dijkstra[v1] + v1_dijkstra[n])
if ans < INF:
    print(ans)
else:
    print(-1)