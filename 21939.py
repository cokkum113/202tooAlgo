from collections import defaultdict
import sys
input = sys.stdin.readline

import heapq

# 문제가 쉬운 순
miniheap = []
# 문제가 어려운 순
maxiheap = []

n = int(input())
diction = defaultdict(list)
for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(maxiheap, [-y, -x])
    heapq.heappush(miniheap, [y, x])
    diction[x].append(y)
    # 큐에 만약 문제번호 7과 100, 7과 300이 있으면 마지막 들어온게 난이도고, 그 난이도가 maxiheap에 있다면 그건 유효한 값

m = int(input())
for _ in range(m):
    ss = input().rstrip().split()
    # 파라미터로  heap만 넣게 하기, 함수로 빼기
    if ss[0] == "recommend":
        if ss[1] == "1":
            if maxiheap:
                while maxiheap:
                    if not maxiheap:
                        break
                    xx = -maxiheap[0][1]
                    if diction[xx]:
                        now_dict = diction[xx]
                        now_validation = now_dict[-1]
                        if now_validation == -maxiheap[0][0]:
                            print(xx)
                            break
                        else:
                            if diction[xx]:
                                now_dict = diction[xx]
                                now_dict.pop()
                    heapq.heappop(maxiheap)

        elif ss[1] == "-1":
            if miniheap:
                while miniheap:
                    if not miniheap:
                        break
                    xx = miniheap[0][1]
                    if diction[xx]:
                        now_dict = diction[xx]
                        now_validation = now_dict[-1]
                        if now_validation == miniheap[0][0]:
                            print(xx)
                            break
                        else:
                            if diction[xx]:
                                now_dict = diction[xx]
                                now_dict.pop()
                    heapq.heappop(miniheap)

    elif ss[0] == "add":
        heapq.heappush(maxiheap, [-int(ss[2]), -int(ss[1])])
        heapq.heappush(miniheap, [int(ss[2]), int(ss[1])])
        diction[int(ss[1])].append(int(ss[2]))

    else:
        if diction[int(ss[1])]:
            diction[int(ss[1])].pop()