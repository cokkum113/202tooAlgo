import sys
input = sys.stdin.readline
import re

s = input().rstrip()
pattern = re.compile('(100+1+|01)+')
ans = pattern.fullmatch(s)

if ans:
    print("SUBMARINE")
else:
    print("NOISE")


