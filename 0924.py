from collections import deque
def p2(origin, new, graph):
    for i in range(51):
        for j in range(51):
            if graph[i][j] == origin:
                graph[i][j] = new
                

def p1(graph,r, c, val):
    graph[r][c] = val

def p4(graph, r, c, r2, c2):
    global remember
    remember.append([graph[r2][c2], r2, c2])
    graph[r2][c2] = graph[r][c]

def p3(r2, c2, remember, graph):
    for i in remember:
        if i[1] == r2 and i[2] == c2:
            graph[r2][c2] = i[0]


remember = []
def solution(commands):
    answer = deque()
    graph = [[''] * (51) for _ in range(51)]
    for i in commands:
        x = i.rstrip().split()
        if x[0] == 'UPDATE':
            if not x[1].isdigit():
                p2(x[1], x[2], graph)
            else:
                if not x[3].isdigit():
                    graph[int(x[1])][int(x[2])] = x[3]
        elif x[0] == 'MERGE':
            p4(graph, int(x[1]), int(x[2]), int(x[3]), int(x[4]))
            
        elif x[0] == 'UNMERGE':
            p3(int(x[1]), int(x[2]), remember, graph)
        elif x[0] == 'PRINT':
            if graph[int(x[1])][int(x[2])] == '':
                answer.append("EMPTY")
            else:
                answer.appendleft(graph[int(x[1])][int(x[2])])
    

    return answer
