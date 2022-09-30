import sys
input = sys.stdin.readline

# 전개도처럼 주사위를 펼쳐서 배열에 저장하고, 
# 인덱스를 주사위의 특정한 면이라고 가정하라. 
# 그리고 굴릴 때마다 해당 인덱스의 값을 교환하거나 변경함으로써 해결할 수 있다

n, m, x, y, k = map(int, input().split())

graph = []
visited = [[False] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))

orderlist = list(map(int, input().split()))

def move(m, qube):
    if m == 1:
        return [0, qube[4],qube[2], qube[1], qube[6], qube[5],qube[3]]
    
    elif m == 2:
        return [0, qube[3], qube[2], qube[6],qube[1], qube[5],qube[4]]
        
    elif m == 3:
        return [0, qube[5], qube[1], qube[3], qube[4], qube[6], qube[2]]
    else:
        return [0, qube[2], qube[6], qube[3], qube[4], qube[1], qube[5]]


dx = [0,0, 0, -1, 1]
dy = [0,1, -1, 0, 0]
# 바닥이 0이면 주사위값이 바닥에 됨
# 바닥이 0이 아니면 주사위에 복사되고 바닥은 0이됨


qube = [0,0,0,0,0,0,graph[x][y]]
for i in orderlist:
    nx = dx[i] + x 
    ny = dy[i] + y 

    if 0 <= nx < n and 0 <= ny < m:
        ss = move(i, qube)
        if graph[nx][ny] == 0:
            graph[nx][ny] = ss[6]
            print(ss[1])
        else:
            ss[6] = graph[nx][ny]
            graph[nx][ny] = 0
            print(ss[1])
    
        x = nx
        y = ny
        qube = ss
        



