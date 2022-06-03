import sys
input = sys.stdin.readline

n = int(input())

# dp = [-1] * (100)

# dp[0] = 0
# dp[1] = 0
# dp[2] = 3
# dp[3] = 0
# dp[4] = 11
# 3개씩 두번 올 수 있는 거 
# 3 * 3
# + 2개 더  =>> 11


# dp[5] = 0
# for i in range(6, 100):
#     if i%2 == 0:
#         dp[i] = (dp[i - 2] * 3) + 
#     else:
#         dp[i] = 0
#여기까지가 솔루션 보기 전

# 솔루션 본 후, 

dp = [0] * 100
dp[0] = 0
dp[1] = 0
dp[2] = 3
dp[3] = 0
dp[4] = 11

for i in range(5, 100):
    if i % 2 == 0:
        dp[i] = (dp[i - 2] * 3) + (sum(dp[:i - 2]) * 2) + 2

    else:
        dp[i] = 0

print(dp[n])