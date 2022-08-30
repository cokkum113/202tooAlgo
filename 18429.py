import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

visited = [False] * n

def bt(index, total):
    global ans
    if index != 0:
        if total < 500:
            return

    if index == n - 1:
        if total >= 500:
            ans += 1
        return
    
    for i in range(n):
        if visited[i]:
            continue
        else:
            visited[i] = True
            total += nums[i]
            bt(index + 1, total - k)
            total -= nums[i]
            visited[i] = False
    
bt(0, 500)
print(ans)
    
    