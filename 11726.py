import sys
input = sys.stdin.readline

n = int(input())

#저장하려고 하니까 dp를 사용하는 것이다.

dp = [0] * (1001)

# dp에 인덱스는 몇개를 사용할때 이고, dp의 값에는 방법의 수가 들어감

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3


for i in range(4, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])