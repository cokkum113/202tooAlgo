import sys
input = sys.stdin.readline

n, k = map(int, input().split())

ll = [[0,0]]

for _ in range(n):
    ll.append(list(map(int, input().split())))

# n번째 물건을 선택할때 jkg이 되는 가치의 최댓값!!!

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if ll[i][0] <= j:
            # 같을때랑 작을때랑 처리가 같음
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - ll[i][0]] + ll[i][1])
        else:
            # 클때 처리도 잘 해줘야함
            dp[i][j] = dp[i - 1][j]

print(dp)
print(max(dp[-1]))