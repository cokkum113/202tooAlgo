import sys
input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
visited = [False] * n

# 문제를 정의해보자 : n까지 다 돌아서의 mini값을 찾은다음에 mini값을 출력
mini = int(1e9)
total = 0
def backtracking(depth, r, c):
    global mini
    global total
    if depth == n and graph[r][c] != 0:
        mini = min(mini, total + graph[r][c])
        return
    
    for i in range(n):
        if visited[i] == False and graph[r][i] != 0:
            visited[i] = True
            total += graph[r][i]
            backtracking(depth + 1, i, c)
            total -= graph[r][i]
            visited[i] = False


for i in range(n):
    visited[i] = True
    backtracking(1, i, i)
    ##################r, c
    visited[i] = False   

print(mini)
