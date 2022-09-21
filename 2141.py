import sys
input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

graph.sort(key = lambda x : x[0])

mid = 0
for city, p in graph:
    mid += p

pp = mid // 2

if mid % 2 != 0:
    pp += 1
    # 2로 안나눠지는 숫자면 올림하기

ans = 0
for city, p in graph:
    ans += p
    
    if ans >= pp:
        break

print(city)
