import sys
input = sys.stdin.readline

graph = []
n = int(input())

for _ in range(n):
    graph.append(list(map(int, input().split())))

mini = int(1e9)

#backtracking으로 뽑고
# 뽑은 걸로 계산하고 이렇게 두개로 풀기

visited = [False] * n

#1. 백트래킹으로 팀 선정하기
def backtracking(index, cnt):
    if cnt == n // 2:
        ans = team_cal()
        return ans
    
    for i in range(index, n):
        if visited[i]:
            continue
        visited[i] = True
        backtracking(i + 1, cnt + 1)
        visited[i] = False

#2. 팀 계산하기
def team_cal():
    global mini
    start_team = []
    link_team = []
    start_score = 0
    link_score = 0

    for i in range(len(visited)):
        if visited[i]:
            start_team.append(i)
        else:
            link_team.append(i)
    
    for i in range(n//2):
        for j in range(i + 1, n//2):
            start_score += graph[start_team[i]][start_team[j]] + graph[start_team[j]][start_team[i]]
            link_score += graph[link_team[i]][link_team[j]] + graph[link_team[j]][link_team[i]]

    mini = min(mini, abs(start_score - link_score))

    return mini

backtracking(0, 0)
print(mini)