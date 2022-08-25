import sys
input = sys.stdin.readline

graph = []

for _ in range(9):
    graph.append(list(map(int, input().split())))

xylist = []

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            xylist.append([i, j])

def check1(x, num):
    for i in range(9):
        if graph[x][i] == num:
            return False
    return True

def check2(y, num):
    for i in range(9):
        if graph[i][y] == num:
            return False
    return True

def check3(x, y, num):
    nx = x // 3 * 3 # 3* 3이 시작하는 부분
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if graph[nx + i][ny + j] == num:
                return False
    
    return True

def backtracking(index):
    if len(xylist) == index:
        for i in range(9):
            print(*graph[i])
        exit()
    
    for i in range(1, 10):
        x = xylist[index][0]
        y = xylist[index][1]

        if check1(x, i) and check2(y, i) and check3(x, y, i):
            graph[x][y] = i
            backtracking(index + 1)
            graph[x][y] = 0

backtracking(0)