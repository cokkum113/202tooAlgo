import sys
input = sys.stdin.readline

n = int(input())

t = [[0]]
for _ in range(n):
    t.append(list(map(int, input().split())))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(len(t[i])):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + t[i][j]
        
        elif j == len(t[i]) - 1:
            dp[i][j] = dp[i - 1][j - 1] + t[i][j]
        
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + t[i][j]

print(max(dp[n]))