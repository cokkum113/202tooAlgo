import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


homes = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            homes.append([i, j])
        if graph[i][j] == 2:
            chicken.append([i, j])

able_c = list(combinations(chicken, m))

realans = int(1e9)
for i in able_c:
    sub_ans = 0
    
    for home in homes:

        mini = int(1e9)
        for j in i:
            x = abs(home[0] - j[0]) + abs(home[1] - j[1])
            if x <= mini:
                mini = x
        sub_ans += mini
    if sub_ans <= realans:
        realans = sub_ans
        
print(realans)