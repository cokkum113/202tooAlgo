import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lines = []
for _ in range(k):
    lines.append(int(input()))
lines.sort()

lo = 1
hi = lines[-1]

while lo <= hi:
    mid = (lo + hi) // 2

    total = 0

    for i in lines:
        total += (i // mid)

    if total >= n:
        lo = mid + 1
    else:
        hi = mid - 1
    
print(hi)