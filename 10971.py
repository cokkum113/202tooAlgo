import sys
input = sys.stdin.readline

n = int(input())

visited = [False] * n
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

mini = int(1e9)
total = 0

# 시작점, 끝점
# 문제 정의 : n까지 다 돌아서 mini값을 찾은 다음에 mini값을 출력
def backtracking(depth, st, v):
    global mini
    global total
    
    if depth == n and graph[st][v] != 0:
        #st에서 v로 오는 길
        mini = min(total + graph[st][v], mini)
    
    for i in range(n):
        if visited[i] == False and graph[st][i] != 0:
            total += graph[st][i]
            visited[i] = True
            backtracking(depth + 1, i, v)
            # depth + 1은 OK
            # i # 시작점이 옮겨간거 OK
            # v는 끝점이니까 두기
            visited[i] = False
            total -= graph[st][i]

for i in range(n):
    visited[i] = True
    backtracking(1, i, i)
    visited[i] = False

print(mini)

