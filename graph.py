#DFS/BFS
#타겟 넘버
from collections import deque
# def solution(numbers, target):
#     answer = 0
#     que = deque()
#     que.append([numbers[0], 0])
#     que.append([-numbers[0], 0])
    
#     while que:
#         x, index = que.popleft()
#         if index == len(numbers) - 1:
#             if x == target:
#                 answer += 1
#         else:
#             index += 1
#             que.append([x + numbers[index], index])
#             que.append([x - numbers[index], index])
    
#     return answer

def solution(n, computers):
    cnt = 0
    visited = [[False] * n for _ in range(n)]
    graph = [0] * n
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                if i != j:
                    graph[i].append(j)
    for i in range(n):
        if visited[i] == False:
            dfs(i, visited, graph)
            cnt += 1
    return cnt

def dfs(cur, visited, graph):
    if visited[cur]:
        return
    visited[cur] = True
    for next in graph[cur]:
        if visited[next] == False:
            dfs(next, visited, graph)
print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))