import sys
input = sys.stdin.readline

n, r, c = map(int,input().split())

cnt = 0
while True:
    if n == 0:
        break
    n -= 1

    if 0 <= r < 2**n and 0 <= c < 2**n:
        cnt += 2**n * 2**n * 0
    
    elif 0 <= r < 2**n and 2**n <= c < 2**(n + 1):
        cnt += 2**n * 2**n * 1
        c -= 2**n
    
    elif 2**n <= r < 2**(n + 1)and 0 <= c <2**n:
        cnt += 2**n * 2**n * 2
        r -= 2**n
    
    elif 2**n <= r < 2**(n + 1)and 2**n <= c <2**(n + 1):
        cnt += 2**n * 2**n * 3
        c -= 2**n
        r -= 2**n

print(cnt)
