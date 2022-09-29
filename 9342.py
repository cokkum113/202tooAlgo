import sys
input = sys.stdin.readline
import re
pattern = re.compile('^[A,B,C,D,E,F]?A+F+C+[A,B,C,D,E,F]?$')

n = int(input())
for _ in range(n):
    s = input().rstrip()
    if pattern.match(s):
        print("Infected!")
    else:
        print("Good")


