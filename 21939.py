from collections import defaultdict
import sys
input = sys.stdin.readline

import heapq

miniheap = []
maxiheap = []

n = int(input())
diction = defaultdict(list)
for _ in range(n):
    x, y = map(int, input().split())
    heapq.heappush(maxiheap, [-y, -x])
    heapq.heappush(miniheap, [y, x])
    diction[x] = y

def recommend(heap):
    while heap:
        xx = 0
        if not heap:
            break
        if heap[0][1] < 0:
            xx = - heap[0][1]
        else:
            xx = heap[0][1]
        
        if diction[xx]:
            now_validation = diction[xx]
            if now_validation == -heap[0][0] or now_validation == heap[0][0]:
                return xx
            else:
                if diction[xx]:
                    diction[xx] = 0
        heapq.heappop(heap)
        
        
m = int(input())
for _ in range(m):
    ss = input().rstrip().split()
    if ss[0] == "recommend":
        if ss[1] == "1":
            print(recommend(maxiheap))

        elif ss[1] == "-1":
            print(recommend(miniheap))

    elif ss[0] == "add":
        heapq.heappush(maxiheap, [-int(ss[2]), -int(ss[1])])
        heapq.heappush(miniheap, [int(ss[2]), int(ss[1])])
        diction[int(ss[1])]= int(ss[2])

    else:
        if diction[int(ss[1])]:
            diction[int(ss[1])] = 0