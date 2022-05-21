import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

#큰거부터 채우는 그리디 아님 , 그러면 옆에 오히려 하나를 사용못하는 상황이 올 수 있음
#그리디로 풀면 예외상황이 많음, 따라서 브루트포스, 백트래킹으로 풀어야함.
graph = []
for i in range(10):
    graph.append(list(map(int, input().split())))

paper = [0] * 5
# 사용할 수 있는 색종이
total = 26

#색종이를 붙일 수 있는 지 판단해야함
def able_paste(x, y, size):
    for i in range(x, x + size + 1):
        for j in range(y, y + size + 1):
            if graph[i][j] == 0:
                return False
                # 0이 나오면 붙일 수 없음 
    return True

# visited 배열 사용할 때처럼
# 색종이를 붙이면 붙은 곳은 1에서 0으로 다 바꿔야함 그렇게해서 맵 전체를 돌면서
# total랑 미니멈값 비교하는 식으로 풀면됨.
def backtracking(x, y, cnt):
    global total
    
    if x >= 10:
        #행까지 다 돌았으니, 이제 값들 비교하면됨
        total = min(total, cnt)
        return
    if y >= 10:
        #열을 끝까지 돌았으니, 다음 행으로 넘어가기, 다음 행으로 넘어갈때는 백트래킹
        backtracking(x + 1, 0, cnt)
        return
    
    #이제 백트래킹의 종료조건이 끝났으니, 이제 백트래킹에서는 무슨일을 하는지
    #구해야함.
    #일단 붙일수있으면, 백트래킹을 돌면서 갯수를 세주면 됨, cnt +1 해서 백트래킹 돌리면됨
    # 색종이를 붙일 수 있는 상황은 1일때
    if graph[x][y] == 1:
        for k in range(5):
            ##########이런 조건 사항들이 문제였음########
            if x + k >= 10:
                continue
            if y + k >= 10:
                continue
            if paper[k] == 5:
                continue
            
            if able_paste(x, y, k):
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        graph[i][j] = 0
                        # 색종이 덮기 

                paper[k] += 1
                backtracking(x, y + k + 1, cnt + 1)
                paper[k] -= 1
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        graph[i][j] = 1
                        # 덮은 색종이 빼기

    else:
        #붙일 수 없는 상황이면 다음 열로 넘어가게해야함
        backtracking(x, y + 1, cnt)
    

backtracking(0, 0, 0)

# print(total)
if total >= 26:
    print(-1)
else:
    print(total)