import sys
input = sys.stdin.readline

n, m = map(int, input().split())


a = n - m

x = max(a, m)
y = min(a, m)

ans = 1
for i in range(n, x, -1):
    ans *= i

for i in range(1, y + 1):
    ans = ans // i
print(ans)
