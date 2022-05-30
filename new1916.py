import sys
input = sys.stdin.readline

#최소비용이니까 MST를 이용하면 됨
#방법은 heapq를 이용하는 방법이 있음

import heapq
heap = []
n = int(input()) #정점의 개수
m = int(input()) #길 이라고 생각하면됨

INF = int(1e9)
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append([cost, b])
    

st, end = map(int, input().split())

cost = [INF] * (n + 1)
cost[st] = 0

visited = [False] * (n + 1)
heapq.heappush(heap, [0, st])

while heap:
    T = heapq.heappop(heap)
    current = T[1]

    if visited[current]:
        continue
    else:
        visited[current] = True
        for next in graph[current]:
            cost[next[1]] = min(cost[next[1]], cost[current] + next[0])
            heapq.heappush(heap, [cost[next[1]], next[1]])

print(cost[end])



