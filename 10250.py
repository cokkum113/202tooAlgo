import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    x = n % h
    y = n // h

    print(x)

    if x == 0:
        print(100 *h + y)
    else:
        print(100 * x + (y + 1))
