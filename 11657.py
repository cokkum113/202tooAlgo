import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = int(1e9)
dis = [INF] * (n + 1)
edge = []

for _ in range(m):
    x, y, dis = map(int, input().split())
    edge.append([x, y, dis])

