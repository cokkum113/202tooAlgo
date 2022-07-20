import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

cnt = 0
while True:
    if n == 0:
        break

    if 0 <= r < 2**(n - 1) and 0 <= c < 2**(n - 1):
        cnt += 2**(n - 1) * 2**(n - 1) * 0

    elif 0 <= r < 2**(n - 1) and 2**(n - 1) <= c < 2**n:
        cnt += 2**(n - 1) * 2**(n - 1) * 1
        c -= 2**(n - 1)
    
    elif 2**(n - 1) <= r < 2**n and 0 <= c < 2**(n - 1):
        cnt += 2**(n - 1) * 2**(n - 1) * 2
        r -= 2**(n - 1)
    
    elif 2**(n - 1) <= r < 2**n and 2**(n - 1) <= c < 2**n :
        cnt += 2**(n - 1) * 2**(n - 1) * 3
        r -= 2**(n - 1)
        c -= 2**(n - 1)
    
    n -= 1

print(cnt)
