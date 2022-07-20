import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

cnt1 = 0
cnt2 = 0
cnt3 = 0

def recursion(x, y, size):
    global cnt1, cnt2, cnt3
    now = graph[x][y]
    flag = False

    for i in range(x, x + size):
        for j in range(y, y + size):
            if now != graph[i][j]:
                flag = True
                # 이때 쪼개서 재귀돌려야함
                break
    
    if flag:
        # 쪼개야되는 부분
        s = size//3
        for i in range(3):
            for j in range(3):
                # 0, 0  0, 3, 0, 6 이렇게 비교할 부분들 순서대로
                recursion(x + i * s, y + j * s, s)
    
    else:
        # 안쪼갠 상태이면
        if now == -1:
            cnt1 += 1
        elif now == 0:
            cnt2 += 1
        else:
            cnt3 += 1

recursion(0, 0, n)
print(cnt1)
print(cnt2)
print(cnt3)