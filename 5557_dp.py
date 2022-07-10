import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n - 1)]
dp[0][numbers[0]] = 1
# dp 초기화, 이 값들은 +,-를 할지말지 상관없이 무조건 들어가야하는 수니까

for i in range(1, n - 1):
    for j in range(21):
        if 0 <= j - numbers[i] <= 20:
            dp[i][j] = dp[i - 1][j - numbers[i]] + dp[i][j]
        if 0 <= j + numbers[i] <= 20:
            dp[i][j] = dp[i - 1][j + numbers[i]] + dp[i][j]
print(dp)