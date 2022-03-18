import sys 
input=sys.stdin.readline 

n, m, x, y, k = map(int, input().split())
dice = [0 for _ in range(7)]
graph = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0 for _ in range(7)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# def move(n, dice):
#     if n == 1:
#         dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5],dice[3]]
#     elif n == 2:
#         dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5],dice[4]]
#     elif n == 3:
#         dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6],dice[2]]
#     elif n == 4:
#         dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1],dice[5]]
#     return dice

for i in range(k): 
    nx = x + dx[order[i]-1] 
    ny = y + dy[order[i]-1] 
    if 0 <= nx < n and 0 <= ny < m: 
        # move(order[i], dice)
        if order[i]==1: 
             dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5],dice[3]]
        elif order[i] == 2:
            dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5],dice[4]]
        elif order[i] == 3:
            dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6],dice[2]]
        elif order[i] == 4:
            dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1],dice[5]]
        if graph[nx][ny]==0: 
            graph[nx][ny]=dice[6] 
        else: 
            dice[6]=graph[nx][ny] 
            graph[nx][ny]=0 
        x=nx 
        y=ny 
        print(dice[1]) 
