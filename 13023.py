import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

flag = False
visited = [False] * (n)

def backtracking(index, pos):
    global flag
    if index >= 4:
        flag = True
        return
    
    visited[pos] = True

    for next in graph[pos]:
        if visited[next] == False:
            backtracking(index + 1, next)
            visited[next] = False

for i in range(n):
    visited[i] = True
    backtracking(0, i)
    visited[i] = False
    if flag:
        break

if flag:
    print(1)
else:
    print(0)





