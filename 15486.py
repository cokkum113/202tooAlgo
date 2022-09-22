import sys
input = sys.stdin.readline

day = [0]
val = [0]
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    day.append(x)
    val.append(y)

dp = [0] * (n + 2)

# 상담을 시작한 경우와 시작 하지 않은 경우
for i in range(1, n + 1):
    dp[i] = max(dp[i - 1], dp[i])
    if i + day[i] <= n + 1:
        # 오늘 상담을 시작하지 않은 경우에 먼저 답이 있을 수 있음.
        dp[i + day[i]] = max(val[i] + dp[i], dp[i + day[i]])
        # dp에 값을 어떻게 저장하면 좋을까 
        # 값이 더해지도록
    
# print(dp)

print(dp[-1])
