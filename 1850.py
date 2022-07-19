import sys
input = sys.stdin.readline

a, b = map(int, input().split())

ca = [1] * a
cb = [1] * b

aa = int(''.join(map(str, ca)))
bb = int(''.join(map(str, cb)))

print(bb % aa)