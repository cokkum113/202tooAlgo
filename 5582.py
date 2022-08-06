import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

s1 = ' ' + s1
s2 = ' ' + s2

dp = [[0] * len(s2) for _ in range(len(s1))]

# dp 정의 : 현재 있는 i 번째의 다른 줄에 있는 j 번째까지 어떻게 몇개가 연속
# 돼서 왔는지, 그 카운터 값이 dp안의 값.

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1

maxi = 0
for i in dp:
    for j in i:
        maxi = max(maxi, j)
print(maxi)