import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    tree = list(map(int, input().split()))

    tree.sort()

    anslist = [0] * n
    c = 0
    if n % 2 != 0:
        for i in range(n//2):
            anslist[n//2] = tree[-1]
            if n // 2 - i < 0 or n // 2 + i > n:
                break
            anslist[n//2 + i + 1] = tree[-(i + 2 + c)]
            anslist[n//2 - i - 1] = tree[-(i + 3 + c)]
            c += 1
    else:
        for i in range(n//2 - 1):
            anslist[n//2] = tree[-1]
            if n//2 - i - 1 < 0 or n//2 + i + 1 > n:
                break
            anslist[n//2 - i - 1] = tree[-(i + 2 + c)]
            anslist[n//2 + i + 1] = tree[-(i + 3 + c)]
            anslist[0] = tree[0]
            c += 1
        
    level = abs(anslist[-1] - anslist[0])
    for i in range(1, n):
        le = abs(anslist[i] - anslist[i - 1])
        level = max(level, le)
    
    print(level)


