import re
import sys
input = sys.stdin.readline

pattern = re.compile('(100+1+|01)+')
n = int(input())

for _ in range(n):
    s = input().rstrip()
    if pattern.fullmatch(s):
        print("YES")
    else:
        print("NO")