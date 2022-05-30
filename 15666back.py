import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ans = []

d = list(set(map(int, input().split())))
d.sort()

visited = [False] * (n + 1)

def backtracking(index):
    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(index, len(d)):
        ans.append(d[i])
        visited[i] = True
        backtracking(i)
        ans.pop()
        visited[i] = False
    

backtracking(0)