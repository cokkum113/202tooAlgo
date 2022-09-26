import sys
input = sys.stdin.readline

graph = []
while True:
    x = input().rstrip()
    if x == "end":
        break

    graph.append(x)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 0]

# 가로
def success_1(x, y, now_i):
    for d in [3, 4]:
        nx = dx[d] + x
        ny = dy[d] + y
        if 0 <= nx <= now_i and 0 <= ny < 9:
            if graph[x][y] != graph[nx][ny]:
                return False
    return True

# 세로
def success_2(x, y, now_i):
    for d in [1, 6]:
        nx = dx[d] + x
        ny = dy[d] + y
        if 0 <= nx <= now_i and 0 <= ny < 9:
            if graph[x][y] != graph[nx][ny]:
                return False
    return True

# 대각선
def success_3(x, y, now_i):
    for d in [0, 2, 5, 7]:
        nx = dx[d] + x
        ny = dy[d] + y
        if 0 <= nx <= now_i and 0 <= ny < 9:
            if graph[x][y] != graph[nx][ny]:
                return False
    return True

for i in range(len(graph)):
    ans_flag = True
    for j in range(9):
        
        if graph[i][j] != '.':
            if success_1(i, j, i) or success_2(i, j, i) or success_3(i, j, i):
                if 'X' in graph[i][j:] or 'O' in graph[i][j:]:
                    ans_flag = False
                    break
                elif 'X' not in graph[i][j:] and 'O' not in graph[i][j:]:
                    ans_flag = True
                    continue
                
        
    if not ans_flag:
        print("invalid")
    else:
        print("valid")
