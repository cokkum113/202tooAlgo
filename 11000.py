import sys
input = sys.stdin.readline
import heapq

n = int(input())
lecture_time = []
for _ in range(n):
    lecture_time.append(list(map(int, input().split())))

lecture_time.sort()
room = []
for i in range(n):
    if room and room[0] <= lecture_time[i][0]:
        heapq.heappop(room)
    heapq.heappush(room, lecture_time[i][1])

print(len(room))