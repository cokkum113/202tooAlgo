import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    que = deque()
    que.append([x, y])
    visited.append([x, y])

    while que:
        xx, yy = que.popleft()
        for next_pos in market:
            if next_pos in visited:
                continue
            else:
                # 이렇게 안들린걸 표시하고
                if abs(xx - next_pos[0]) + abs(yy - next_pos[1]) <= 20 * 50:
                    if next_pos[0] == fest_x and next_pos[1] == fest_y:
                        return 1
                    que.append([next_pos[0], next_pos[1]])
                    visited.append([next_pos[0], next_pos[1]])
    return 0
                



t = int(input())
for _ in range(t):
    n = int(input())
    market = []
    home_x, home_y = map(int, input().split())
    visited = []
    # visited좌표를 만드는 것보다 거기에 갔는 지 안갔는지니까
    # 리스트로 넣는다. 리스트에 들어가있다면 들린거니까 안들리면된다.
    for _ in range(n):
        market.append(list(map(int, input().split())))
    
    fest_x, fest_y = map(int, input().split())
    market.append([fest_x, fest_y]) # 이것도 다음 들릴꺼니까 여기안에 넣기
    # 만약 fest_x, fest_y이면 도착한거니까!!

    if bfs(home_x, home_y) == 1:
        print("happy")
    else:
        print("sad")
        
    

