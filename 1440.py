import sys
input = sys.stdin.readline
from itertools import permutations

# cnt = 6
# s = input().rstrip()

# x = s.split(':')

# for i in x:
#     if i == '00':
#         cnt -= 2
#     elif int(i) > 24:
#         cnt -= 2
#     elif int(i) > 12:
#         cnt -= 2

cnt = 0
s = input().rstrip()
x = s.split(':')
ss = list(permutations(x, 3))
for i in ss:
    if 0 < int(i[0]) <= 12 and 0 <= int(i[1]) <= 59 and 0 <= int(i[2]) <= 59:
        cnt += 1
print(cnt)
