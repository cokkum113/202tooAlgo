from curses import REPORT_MOUSE_POSITION
import sys
input = sys.stdin.readline
import heapq

n = int(input())
room = []

for _ in range(n):
    room.append(list(map(int, input().split())))

room.sort(key=lambda x : x[0])

heap = []
heapq.heappush(heap, room[0][1])

for i in range(1, n):
    if len(heap) != 0 and room[i][0] < heap[0]:
        heapq.heappush(heap, room[i][1])
    elif len(heap) != 0:
        heapq.heappop(heap)
        heapq.heappush(heap, room[i][1])
    
print(len(heap))