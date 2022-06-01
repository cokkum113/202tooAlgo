from operator import ne
import sys
input = sys.stdin.readline

tc = int(input())
INF = int(1e9)
# 벨만포드

# n - 1 번 반복하면서 모든!! 모든 간선을 확인
#      각 간선을 거쳐 다른 노드로 가는 비용을 계산해서 최단 거리 테이블 갱신
# 만약 음수 간선 순환이 발생하는 지 체크하고 싶으면 한번 더 수행
# 최단거리 테이블이 갱신되면 음수 간선 순환이 존재하는 것!!

def bellmanford(st):
    dis[st] = 0
    for search in range(1, n + 1):
        for index in range(1, n + 1):
            for next, T in graph[index]:
                if dis[next] > dis[index] + T:
                    dis[next] = dis[index] + T
                    if search == n:
                        return True
    return False


for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    dis = [INF] * (n + 1)

    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])
    
    for _ in range(w):
        ws, we, wt = map(int, input().split())
        graph[ws].append([we, -wt])

    if bellmanford(1):
        print("YES")
    else:
        print("NO")
    