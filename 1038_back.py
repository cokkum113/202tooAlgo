import sys
input = sys.stdin.readline

n = int(input())
cnt = 9
def backtracking(depth, limit, temp):
    global cnt

    if depth == limit:
        cnt += 1
        
        if cnt == n:
            print(temp)
            exit()
        
    for i in range(int(temp[-1])):
        backtracking(depth + 1, limit, temp + str(i))

if n < 10:
    print(n)
    exit()
else:
    for k in range(1, 11):
        for kk in range(1, 10):
            backtracking(0, k, str(kk))

print(-1)
