import heapq
import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
INF = int(1e9)

for _ in range(m):
    sp, dp, w = map(int, input().split())
    graph[sp].append([w, dp])

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        time, pos = heapq.heappop(q)
        if distance[pos] < time:
            continue
        for next_time, next_pos in graph[pos]:
            cost = next_time + time
            if distance[next_pos] > cost:
                distance[next_pos] = cost
                heapq.heappush(q, [cost, next_pos])
    return distance

ans = []
for i in range(1, n + 1):
    one_dijkstra = dijkstra(i)
    two_dijkstra = dijkstra(x) # 돌아올때
    ans.append(one_dijkstra[x] + two_dijkstra[i])

print(max(ans))

