def solution(rows, columns, queries):
    answer = []
    
    graph = [[0] * (columns + 1) for _ in range(rows + 1)]
    cnt = 1
    
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            graph[i][j] = cnt
            cnt += 1
    for x1, y1, x2, y2 in queries:
        temp = graph[x1][y1]
        mini = temp
        
        #left
        for i in range(x1, x2):
            a = graph[i + 1][y1]
            graph[i][y1] = a
            mini = min(mini, a)
        #bottom
        for i in range(y1, y2):
            a = graph[x2][i + 1]
            graph[x2][i] = a
            mini = min(mini, a)
        
        
        #right
        for i in range(x2, x1, -1):
            a = graph[i - 1][y2]
            graph[i][y2] = a
            mini = min(mini, a)
         #top
        for i in range(y2, y1, -1):
            a = graph[x1][i - 1]
            graph[x1][i] = a
            mini = min(mini, a)
            
        
        
        graph[x1][y1 + 1] = temp
        answer.append(mini)
        
    return answer