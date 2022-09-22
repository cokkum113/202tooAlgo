import sys
input = sys.stdin.readline

c, n = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))
