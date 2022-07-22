import sys
input = sys.stdin.readline

ss= list(map(int, input().split()))
ss.sort()
a = ss[0]
b = ss[1]

# ca = int('1' * a)
# cb = int('1' * b)

def gcd(x, y):
    while y > 0:
        x, y = y, x%y
    return x

print('1' * gcd(a, b))

