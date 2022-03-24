import sys
input = sys.stdin.readline

n = int(input())

dp1 = [0] * 3
dp2 = [0] * 3

mini = [0] * 3
maxi = [0] * 3

for i in range(n):
    x, y, z = map(int, input().split())
    for j in range(3):
        if j == 0:
            maxi[j] = x + max(dp1[j], dp1[j + 1])
            mini[j] = x + min(dp2[j], dp2[j + 1])
        elif j == 1:
            maxi[j] = y + max(dp1[j - 1], dp1[j + 1], dp1[j])
            mini[j] = y + min(dp2[j], dp2[j + 1], dp2[j - 1])
        elif j == 2:
            maxi[j] = z + max(dp1[j], dp1[j - 1])
            mini[j] = z + min(dp2[j], dp2[j - 1])
        
    for j in range(3):
        dp1[j] = maxi[j]
        dp2[j] = mini[j]

ans1 = max(dp1)
ans2 = min(dp2)
print(ans1, ans2)
        