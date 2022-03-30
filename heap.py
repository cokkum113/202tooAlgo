#더 맵게
import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            break
        x = heapq.heappop(scoville)
        #10^6
        y = heapq.heappop(scoville)
        #10^6
        z = x + 2*y
        heapq.heappush(scoville, z)
        #10^6
        cnt += 1
        
        if len(scoville) == 1 and scoville[0] < K:
            # 1걸리는게 10^6개
            return -1
    return cnt
    #10^6

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
    
    #힙은 다 1씩이니까 input 개수만큼 걸리는거 아닌지
                
    
#디스크 컨트롤러
import heapq
def solution(jobs):
    answer = 0
    start = -1
    cur = 0
    cnt = 0
    ans = []
    
    while True:
        if len(jobs) == cnt:
            break
        for i in jobs:
            if i[0] > start and i[0] <= cur:
                heapq.heappush(ans, (i[1], i[0]))
        
        if len(ans) > 0:
            a = heapq.heappop(ans)
            
            start = cur
            cur += a[0]
            answer = answer + cur - a[1]
            cnt += 1
        else:
            cur += 1
            
    answer = answer // len(jobs)
    return answer