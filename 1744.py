import sys
input = sys.stdin.readline

n = int(input())
plus = []
minus = []
zero = []
total = 0

for _ in range(n):
    x = int(input())
    if x > 1:
        plus.append(x)
    elif x < 1:
        minus.append(x)
    elif x == 1:
        # zero.append(x)
        total += 1

plus.sort()
minus.sort()

if len(plus) % 2 == 0:
    for i in range(len(plus) - 1, -1, -2):
        x = plus[i] * plus[i - 1]
        total += x
else:
    for i in range(len(plus) - 1, 0, -2):
        x = plus[i] * plus[i - 1]
        total += x
    total += plus[0]

if len(minus) % 2 == 0:
    for i in range(len(minus) - 1, -1, -2):
        x = minus[i] * minus[i - 1]
        total += x
else:
    for i in range(len(minus) - 1, 0, -2):
        x = minus[i] * minus[i - 1]
        total += x
    total += minus[0]

print(total)


    