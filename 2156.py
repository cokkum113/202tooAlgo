import sys
input = sys.stdin.readline

n = int(input())
wine = []
for _ in range(n):
    wine.append(int(input()))

dp = [0] * n

if n == 1:
    print(wine[0])
elif n == 2:
    print(wine[0] + wine[1])
elif n == 3:
    print(max(wine[0] + wine[2], wine[1] + wine[2], wine[0] + wine[1]))

else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], wine[0] + wine[1])
    dp[3] = max(dp[2], wine[3] + dp[1], wine[3] + wine[2] + wine[0], wine[3] + wine[1] + wine[0])
    
    for i in range(4, n):
        dp[i] = max(wine[i] + wine[i - 1] + dp[i - 3], wine[i] + dp[i - 2], wine[i - 1] + wine[i - 2]+ dp[i - 4])
        
    print(dp[n - 1])
