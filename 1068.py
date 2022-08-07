import sys
input = sys.stdin.readline

n = int(input())
xlist = list(map(int, input().split()))

remove_x = int(input())

graph = [[] for _ in range(51)]

for i in range(len(xlist)):
    if xlist[i] == -1:
        graph[50].append(i)
    else:
        graph[xlist[i]].append(i)

visited = [False] * 51
cnt = 0

def dfs(current, remove_x):
    global cnt
    if visited[current]:
        return

    visited[current] = True

    if remove_x in graph[current]:
        graph[current].remove(remove_x)
    
    if current == remove_x:
        graph[current] = []
    
    for next in graph[current]:
        dfs(next, remove_x)
    
    # 여기에 적는 게 현재노드에 상태, 할일!
    if len(graph[current]) == 0 and current != remove_x and current != 50:
        cnt += 1 

dfs(50, remove_x)
print(cnt)