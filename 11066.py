import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    files = [0] + list(map(int, input().split()))
    dp = [[0] * (k) for _ in range(k)]

    #누적합
    total = [0]
    for i in files:
        total.append(total[-1] + i)
    
    