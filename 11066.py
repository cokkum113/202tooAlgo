import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    files = [0] + list(map(int, input().split()))
    dp = [[0] * (k + 1) for _ in range(k + 1)]
    ans = [0] * (k + 1) 

    files.sort()

    for i in range(1, k + 1):
        dp[i][0] = files[i]

    for i in range(1, k+ 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
    
print(dp)