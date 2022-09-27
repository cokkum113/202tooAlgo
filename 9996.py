import sys
input = sys.stdin.readline

n = int(input())
pattern = input().rstrip()

p = pattern.split('*')

for _ in range(n):
    s = input().rstrip()
    s1 = s[:len(p[0])]
    s2 = s[-len(p[1]):]

    if len(s) < len(p):
        print("NE")
    else:
        if s1 == p[0] and s2 == p[1] and len(s) >= len(p):
            print("DA")
        else:
            print("NE")