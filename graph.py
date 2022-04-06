#DFS/BFS
#타겟 넘버
from collections import deque
def solution(numbers, target):
    answer = 0
    que = deque()
    que.append([numbers[0], 0])
    que.append([-numbers[0], 0])
    
    while que:
        x, index = que.popleft()
        if index == len(numbers) - 1:
            if x == target:
                answer += 1
        else:
            index += 1
            que.append([x + numbers[index], index])
            que.append([x - numbers[index], index])
    
    return answer

#네트워크
def solution(n, computers):
    cnt = 0
    visited = [False] * n
    
    for i in range(n):
        if visited[i] == False:
            dfs(i, visited, computers, n)
            cnt += 1
    return cnt

def dfs(cur, visited, computers, n):
    if visited[cur]:
        return
    visited[cur] = True
    for next in range(n):
        if visited[next] == False and computers[cur][next] == 1 and next != cur:
            dfs(next, visited, computers, n)

#단어변환 ###########이게 제일 어려웠음
from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words)
    que = deque()
    que.append([begin, 0])
    
    if target not in words:
        return 0
    
    while que:
        w, cnt = que.popleft()
        if w == target:
            return cnt
        for i in range(len(words)):
            tmp = 0
            if visited[i] == False:
                for j in range(len(w)):
                    if w[j] != words[i][j]:
                        tmp += 1
                if tmp == 1:
                    que.append([words[i], cnt + 1])
                    visited[i] = True
                        
    return cnt

#여행경로
def solution(tickets):
    answer = []
    route = dict()
    for x, y in tickets:
        if x in route:
            route[x].append(y)
        else:
            route[x] = [y]
    for i in route.keys():
        route[i].sort(reverse = True)
        
    stack = ["ICN"]
    while stack:
        r = stack[-1]
        
        if r not in route or len(route[r]) == 0:
            s = stack.pop()
            answer.append(s)
        else:
            stack.append(route[r].pop())
            
            
    return answer[::-1]

