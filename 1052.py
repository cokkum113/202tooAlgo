import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def buy(num):
    cnt = 0
    while True:
        a = num //2
        b = num % 2
        cnt += b
        num = a
        if num == 0:
            break
    return cnt


plus = n
while True:
    if buy(plus) <= k:
        print(plus - n)
        break
    else:
        plus += 1
