import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

s1 = ' ' + s1
s2 = ' ' + s2

# i번째의 위치에 있을 때, j번째 수까지 제일 최장 거리를 구하기

dp = [[0] * (len(s2)) for _ in range(len(s1))]

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(max(dp[-1]))