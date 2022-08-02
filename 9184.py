import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


dp = [[[0 for _ in range(51)] for _ in range(51)] for _ in range(51)]

def w(a, b, c):
    global dp
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if a < b and b < c:
        if dp[a][b][c]:
            return dp[a][b][c]
        else:
            dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        # return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return dp[a][b][c]
    
    else:
        if dp[a][b][c]:
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
