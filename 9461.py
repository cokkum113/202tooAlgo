from random import randrange
import sys
input =  sys.stdin.readline

dp = [0] * 101

dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(3, 101):
    dp[i] = dp[i - 3] + dp[i - 2]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
    