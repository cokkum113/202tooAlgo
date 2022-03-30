#더 맵게
import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            break
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        z = x + 2*y
        heapq.heappush(scoville, z)
        cnt += 1
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
        
    return cnt

#이중 우선순위 큐
import heapq
from collections import deque
def solution(operations):
    answer = []
    maxheap = []
    for i in operations:
        if i[0] == "I":
            x = int(i[2:])
            heapq.heappush(answer, x)
            heapq.heappush(maxheap, (-x, x))
            
        if i[0] == "D":
            if len(answer) != 0:
                if i[2:] == "1": 
                    maxi = heapq.heappop(maxheap)
                    maxi = maxi[1]
                    answer.remove(maxi)
                else:
                    m = heapq.heappop(answer)
                    maxheap.remove((-m, m))
    if len(answer) == 0:
        return [0,0]
    else:
        return [heapq.heappop(maxheap)[1], heapq.heappop(answer)]
                
         