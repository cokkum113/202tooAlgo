from itertools import combinations
import sys
input = sys.stdin.readline
import copy

n, m, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

#성에 궁수 세명 배치
killer = [i for i in range(m)]
killer_pos = list(combinations(killer, 3))

#궁수는 하나의 적을 공격가능위치
#공격가능한 리스트 뽑기
def attack(kk):
    able_list = []
    kills = 0
    for k in kk:
        rr = []
        for i in range(n):
            for j in range(m):
                if copygraph[i][j] == 1:
                    dis = abs(n - i) + abs(k - j)
                    if dis <= d:
                        rr.append([dis, i, j])
                    # 가능한 것들을 넣어줌
        rr.sort(key=lambda x : (x[0], x[2]))
        if rr:
            # print(rr)
            able_list.append(rr[0])
            #나중에 이 부분 지워보기
            #제거 해야할 적을 아예 이때 넣어줌
    for a in able_list:
        distance, x, y = a
        if copygraph[x][y] == 1:
            copygraph[x][y] = 0
            kills += 1
    return kills


# for i in killer_pos:
#     x = able_kill_list(i)
#     print(x)


#모든 궁수는 동시에 공격 -> 한번에 1이 0이 됨

#적의 이동과 적의위치 반환
def move_enemy():
    for i in range(-1, -n, -1):
        copygraph[i] = copygraph[i - 1]

    copygraph[0] = [0] * m


def is_empty():
    for i in range(n):
        for j in range(m):
            if copygraph[i][j] == 1:
                return False
    return True

maxi = 0
for ki in killer_pos:
    copygraph = copy.deepcopy(graph)
    cnt = 0
    while not is_empty():
        cnt += attack(ki)
        move_enemy()
    
    maxi = max(maxi, cnt)
print(maxi)
        


