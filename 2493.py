import sys
input = sys.stdin.readline

# 현재시점에서만 상관있는걸 보면되는 상태?
n = int(input())
top = list(map(int, input().split()))

stack = []
ans = [0] * n
for i in range(n):
    # 나보다 작은 거 빼기
    while stack and stack[-1][1] < top[i]:
        stack.pop()
    
    if not stack:
        ans[i] = 0
    else:
        ans[i] = stack[-1][0]
    

    stack.append([i + 1,top[i]])

print(' '.join(map(str,ans)))