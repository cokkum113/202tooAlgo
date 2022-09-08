from collections import defaultdict
import sys
input = sys.stdin.readline
import heapq

t = int(input())
for _ in range(t):
    xx = int(input())
    maxiheap = []
    miniheap = []
    diction = defaultdict(int)
    
    for _ in range(xx):
        s, num = input().rstrip().split()
        
        num = int(num)
        
        if s == 'I':
            heapq.heappush(maxiheap, -num)
            heapq.heappush(miniheap, num)
            diction[num] += 1
        
        else:
            if num == -1:
                while True:
                    if not miniheap:
                        break
                    xx = miniheap[0]
                    if diction[xx] != 0:
                        diction[xx] -= 1
                        heapq.heappop(miniheap)
                        break
                    else:
                        heapq.heappop(miniheap)
            else:
                while True:
                    if not maxiheap:
                        break
                        
                    xx = maxiheap[0]
                    if diction[-xx] != 0:
                        diction[-xx] -= 1
                        heapq.heappop(maxiheap)
                        break
                    else:
                        heapq.heappop(maxiheap)
    
    total = 0
    xxx = []
    mini = 0
    maxi = 0
    for i in diction:
        total += diction[i]
    
    if total == 0:
        print("EMPTY")

    else:
        for i in diction:
            xxx.append(i)
        xxx.sort()
        for i in xxx:
            if diction[i] != 0:
                mini = i
                break
        xxx = xxx[::-1]
        for i in xxx:
            if diction[i] != 0:
                maxi = i
                break
        # print(xxx)
        print(maxi, mini)
    
            

    

            
                
