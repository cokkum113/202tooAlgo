from itertools import permutations
import sys
input = sys.stdin.readline

s = list(input().rstrip())
s.sort(reverse = True)
ss = []
# ss = permutations(s, len(s))
if s.count('0') == 0:
    print(-1)
    exit()

else:
    for i in s:
        ss.append(int(i))

if sum(ss) % 3 == 0:
    print(int(''.join(s)))
else:
    print(-1)