# dp문제는 인덱스를 뭐를 잡고 갈 것인지가 중요
import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
# 가장 긴 숫자까지 어떻게 길게 왔는지 계속더해가는 식으로 풀면 될듯하다

# a를 크게 돌면서 b를 돌면서 어느 길이에서 어떻게 끊기는 지 보면될거같다

a = ' ' + a
b = ' ' + b

dp = [[0] * len(b) for _ in range(len(a))]


# print(a, b)

# 문자열1을 하나를 잡고 돌 때
# 문자열2에 있는 값이 맞으면 그 전꺼중에 제일 큰 값과 더해주기
for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
#dp[-1]이 4가 나와야지 정상
print(max(dp[-1]))