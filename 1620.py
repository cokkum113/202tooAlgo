import sys
input = sys.stdin.readline

n, m =  map(int, input().split())

names = dict()
indexing = dict()

for i in range(1, n + 1):
    s = input().rstrip()
    names[i] = s
    indexing[s] = i

for i in range(m):
    s = input().rstrip()
    if ord('A') <= ord(s[0]) <= ord('Z'):
        print(indexing[s])
    else:
        print(names[int(s)])
