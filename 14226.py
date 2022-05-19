import sys
input = sys.stdin.readline
from collections import deque
s = int(input())


### 997을 쓰면 안됨
# dp = [[0] * 2001 for _ in range(2001)]
# 걸리는 시간 dp
# 이모티콘 만들기
visited = [[False] * 1001 for _ in range(1001)]

def bfs():
    que = deque()
    que.append([1, 0, 0]) # 화면, 클립보드 , 카운트수
    visited[1][0] = True # 화면1개, 클립보드0개는 방문했음

    while que:
        hwa, clip, cnt = que.popleft()
        
        if hwa == s:
            return cnt
        
        for i in range(3):
            if i == 0:
                n_hwa = hwa
                n_clip = hwa
            elif i == 1:
                n_hwa = hwa + clip
                n_clip = clip

            elif i == 2:
                n_hwa = hwa - 1
                n_clip = clip
            
            if n_hwa >= 1001 or n_clip >= 1001 or n_hwa < 0 and n_clip < 0 or visited[n_hwa][n_clip] == True:
                continue
            visited[n_hwa][n_clip] = True
            que.append([n_hwa , n_clip, cnt + 1])
        

print(bfs())
