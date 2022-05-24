import sys
input = sys.stdin.readline

n = int(input())
rooms = []
for _ in range(n):
    ll = list(map(int, input().split()))
    rooms.append(ll)
rooms = sorted(rooms, key=lambda x : (x[1], x[0]))

x = rooms[0][1]
cnt = 1
for i in range(1, n):
    if rooms[i][0] >= x:
        cnt += 1
        x = rooms[i][1]
    else:
        continue

print(cnt)