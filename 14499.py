import sys 
input=sys.stdin.readline 

n, m, x, y, k = map(int, input().split())
dice = [0 for _ in range(7)]
graph = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def move(n, dice):
    if n == 1:
        return [0, dice[4], dice[2], dice[1], dice[6], dice[5],dice[3]]
    if n == 2:
        return [0, dice[3], dice[2], dice[6], dice[1], dice[5],dice[4]]
    if n == 3:
        return [0, dice[5], dice[1], dice[3], dice[4], dice[6],dice[2]]
    if n == 4:
        return [0, dice[2], dice[6], dice[3], dice[4], dice[1],dice[5]]
    
for i in range(k): 
    nx = x + dx[order[i]] 
    ny = y + dy[order[i]] 
    if 0 <= nx < n and 0 <= ny < m: 
        newdice = move(order[i], dice)
        if graph[nx][ny]==0: 
            graph[nx][ny]=newdice[6] 
        else: 
            newdice[6]=graph[nx][ny] 
            graph[nx][ny]=0 
        x=nx 
        y=ny 
        dice = newdice

        print(newdice[1]) 
    
