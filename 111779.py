import sys
input = sys.stdin.readline
import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
INF = int(1e9)
distance = [INF] * (n + 1)

for _ in range(m):
    st, e, w = map(int, input().split())
    graph[st].append([w, e])

start, end = map(int, input().split())
parent = [i for i in range(n + 1)]

def dijkstra(start):
    heap = []
    heapq.heappush(heap, [0, start])
    distance[start] = 0

    while heap:
        cost, pos = heapq.heappop(heap)
        if distance[pos] < cost:
            continue
        for next_cost, next_pos in graph[pos]:
            if distance[next_pos] > cost + next_cost:
                distance[next_pos] = cost + next_cost
                heapq.heappush(heap, [distance[next_pos], next_pos])
                parent[next_pos] = pos

dijkstra(start)
print(distance[end])

ans = []
temp = end
while True:
    ans.append(temp)
    if temp == parent[temp]:
        break
    temp = parent[temp]

print(len(ans))
ans.reverse()
print(*ans)
                
