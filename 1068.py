import sys
input = sys.stdin.readline

v = int(input())
xlist = list(map(int, input().split()))

remove_x = int(input())

graph = [[] for _ in range(51)]

for i in range(v):
    if xlist[i] == -1:
        graph[50].append(i)
    
    elif xlist[i] != -1 and xlist[i] != remove_x:
        graph[xlist[i]].append(i)
visited = [False] * 51

cnt = 0
def dfs(current):
    global cnt
    # 여기에 코드 현재시점에서 실행할 코드
    if visited[current]:
        return
    
    visited[current] = True

    if len(graph[current]) == 0 and current != remove_x:
        cnt += 1
    
    # 다음으로 가기
    for next in graph[current]:
        dfs(next)

    # 여기에도 갔다와서 실행할 코드
    


dfs(50)
print(cnt)