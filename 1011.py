import sys
input = sys.stdin.readline
from collections import deque

# y지점의 직전 거리는 반드시 1광년이니까
# y - 1까지 가면 될 거 같음.
# y - 1까지 가야하는 걸 잊지말기

def bfs(index):
    q = deque()
    q.append([index, 0])
    visited[index] = True
    offset = 0

    while q:
        posx, cnt = q.popleft()

        if posx == y - 1 or posx == y + 1:
            return cnt

        if posx + (offset + 1) <= (2**31) and visited[posx + (offset + 1)] == False:
            visited[posx + (offset + 1)] = True
            q.append([posx + (offset + 1), cnt + 1])
            offset += 1
        
        if posx + offset <= (2**30) and visited[posx + offset] == False:
            visited[posx + offset] = True
            q.append([posx + offset, cnt + 1])

        if offset - 1 >= 0 and posx + (offset - 1) <= (2**31) and visited[posx + (offset - 1)] == False:
            visited[posx + (offset - 1)] = True
            q.append([posx + (offset - 1), cnt + 1])
            offset -= 1
        
        if x <= posx - offset and visited[posx - offset] == False:
            visited[posx - offset] = True
            cnt += 1
            q.append([posx - offset, cnt])
        
        if x <= posx - (offset+1) and visited[posx - (offset+1)] == False:
            visited[posx - (offset+1)] = True
            q.append([posx - (offset+1), cnt + 1])
            offset += 1

        if offset - 1 >= 0 and x <= posx - (offset-1) and visited[posx - (offset-1)] == False:
            visited[posx - (offset-1)] = True
            q.append([posx - (offset-1), cnt + 1])
            offset -= 1
        
        
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    visited = [False] * (2**31)
    # 뒤로도 갈 수 있으니까, 아예 2^31만큼 크게 만들어주고
    a = bfs(x)
    print(a + 1)
