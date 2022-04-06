#가장 먼 노드
from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] * (n + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    maxi = 0
    ans = []
    que = deque()
    que.append([1, 0])
    visited[1] = True
    while que:
        pos, cnt = que.popleft()
        for i in graph[pos]:
            if visited[i] == False:
                visited[i] = True
                que.append([i, cnt + 1])
        ans.append(cnt)
    a = max(ans)
    answer = ans.count(a)
    return answer

#순위
from collections import defaultdict

def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    
    for i in results:
        win[i[0]].add(i[1])
        lose[i[1]].add(i[0])
    
    for i in range(1, n + 1):
        for w in lose[i]:
            win[w].update(win[i])
        for l in win[i]:
            lose[l].update(lose[i])
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            answer += 1
    return answer