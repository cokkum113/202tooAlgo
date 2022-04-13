import sys
sys.setrecursionlimit(10**5)
def solution(N, number):
    answer = 9

    return answer

def backtracking(prev, cnt, number, N):
    if prev == number:
        answer = min(answer, cnt)
        return 
######################백트래킹_ n으로 표현

def solution(N, number):
    answer = 0
    
    if N == number:
        return 1
    
    anslist = [0, [N]]
    for i in range(2, 9):
        nums = [int(str(N) * i)]
        
        for j in range(1, i // 2 + 1):
            
            for x in anslist[j]:
                for y in anslist[i - j]:
                    nums.append(x + y)
                    nums.append(x - y)
                    nums.append(x * y)
                    if y != 0:
                        nums.append(x//y)
                    if x != 0:
                        nums.append(y//x)
        print(nums, i, j)
        if number in nums:
            return i
        anslist.append(nums)
    
    return -1
solution(5, 12)

#정수삼각형
def solution(triangle):
    answer = 0
    
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    
    dp[0][0] = triangle[0][0]
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])
    
    return max(dp[-1])

#등굣길 #####틀린 코드
from collections import deque
def solution(m, n, puddles):
    answer = 0
    
    graph = [[0] * m for _ in range(n)]
    
    for i in puddles:
        x, y = i
        graph[x - 1][y - 1] = 'z'
    graph[0][0] = 1
    
    
    que = deque()
    que.append([0, 0])
    
    dx = [0, 1]
    dy = [1, 0]
    
    while que:
        x, y = que.popleft()
        
        for d in range(2):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 'z':
                    continue
                graph[nx][ny] += graph[x][y]
                if [nx, ny] not in que:
                    que.append([nx, ny])
                    
    return graph[n - 1][m - 1] % 1000000007


#######맞은 코드
def solution(m, n, puddles):
    answer = 0
    
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    
    graph[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [j, i] in puddles:
                continue
            graph[i][j] += graph[i -1][j] + graph[i][j - 1]
            
    return graph[n][m] % 1000000007