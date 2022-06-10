import sys
input = sys.stdin.readline
import heapq

time = []
n = int(input())
for _ in range(n):
    time.append(list(map(int, input().split())))


time.sort(key = lambda x : (x[0], x[1]))

heap = []
heapq.heappush(heap, time[0][1])

for i in range(1, n):
    if len(heap) != 0 and time[i][0] < heap[0]:
        heapq.heappush(heap, time[i][1])
    elif len(heap) != 0:
        heapq.heappop(heap)
        heapq.heappush(heap, time[i][1])

print(len(heap))