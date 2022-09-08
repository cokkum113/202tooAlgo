import sys
input = sys.stdin.readline
import heapq

n = int(input())
nums = []
for _ in range(n):
    x = int(input())
    
    if x == 0:
        if nums:
            yy = heapq.heappop(nums)
            print(-yy)
        else:
            print(0)
    else:
        heapq.heappush(nums, -x)
        
