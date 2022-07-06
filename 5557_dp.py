import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
#백트래킹으로 저장할 부분을 잘 생각해보기
# 다시 안가고 저장할 부분!
dp = [[0] * 21 for _ in range(n - 1)]

#dp는 그럼 값들을 저장되고 있는 것이다. sum들의 값이 아니라 개수의 값


# 솔루션

dp[0][nums[0]] = 1

for i in range(1, n - 1):
    for j in range(21):
        if dp[i - 1][j] != 0:
            pre_val = j
            next_val = nums[i]

            if 0 <= pre_val + next_val <= 20:
                dp[i][pre_val + next_val] += dp[i - 1][pre_val]
            if 0 <= pre_val - next_val <= 20:
                dp[i][pre_val - next_val] += dp[i - 1][pre_val]

print(dp[n - 2][nums[-1]])