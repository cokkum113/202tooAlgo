from curses.ascii import isdigit
import sys
input = sys.stdin.readline
from collections import deque

#입력이 10^6이니까 완전 탐색이 아님

F, S, G, U, D = map(int, input().split())

visited = [False] * (F + 1)

# 이거 bfs로 풀수 있음, 숨바꼭질처럼!!

def bfs(st):
    que = deque()
    que.append([st, 0])
    visited[st] = True

    while que:
        x, cnt = que.popleft()

        if x == G:
            return cnt

        if x + U <= F and visited[x + U] == False:
            que.append([x + U, cnt + 1])
            visited[x + U] = True
        if 1 <= x - D and visited[x - D] == False:
            que.append([x - D, cnt + 1])
            visited[x - D] = True

ans = bfs(S)
if str(ans).isdigit():
    print(ans)
else:
    print("use the stairs")





    
