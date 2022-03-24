import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

garo = 1
sero = 2
dae = 3
ans = 0

def dfs(x, y, a):
    global ans
    if x == n - 1 and y == n - 1:
        ans += 1
        return
        
    if a == garo:
        if y + 1 < n and graph[x][y + 1] == 0:
            dfs(x, y + 1, garo)
        if y + 1 < n and x + 1 < n and graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0:
            dfs(x + 1, y + 1, dae)
    elif a == sero:
        if x + 1 < n and graph[x + 1][y] == 0:
            dfs(x + 1, y, sero)
        if x + 1 < n and y + 1 < n and graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0:
            dfs(x + 1, y + 1, dae)
    elif a == dae:
        if x + 1 < n and graph[x + 1][y] == 0:
            dfs(x + 1, y, sero)
        
        if y + 1 < n and graph[x][y + 1] == 0:
            dfs(x, y + 1, garo)
        
        if x + 1 < n and y + 1 < n and graph[x + 1][y + 1] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y] == 0:
            dfs(x + 1, y + 1, dae)

dfs(0, 1, garo)      
print(ans)
        