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
# 유클리드 호제법은 알겠는데, 이 1을 곱하는 방식이 이해가 안된다
# 1을 곱해서 어떻게 답이 나오는지 이해가 되지 않는다. 