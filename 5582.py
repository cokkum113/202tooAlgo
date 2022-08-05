import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

s1 = ' ' + s1
s2 = ' ' + s2

a, b = max(len(s1), len(s2)), min(len(s1), len(s2))

print(a, b)