import sys
input = sys.stdin.readline

dp = [[[1 for _ in range(51)] for _ in range(51)] for _ in range(51)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        return w(a, b, c)
    
    elif a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        # return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]
    
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        # return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]

while True:
    x, y, z = map(int, input().split())
    if x == -1 and y == -1 and z == -1:
        break
    aa = w(x, y, z)
    print("w(%d, %d, %d) = %d" %(x, y, z, aa))
