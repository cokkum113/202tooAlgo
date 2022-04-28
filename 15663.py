import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

ans = []
visited = [False] * n

def backtracking(index):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    aa = 0
    
    for i in range(n):
        if visited[i] == False and aa != nums[i]:
            ans.append(nums[i])
            visited[i] = True
            aa = nums[i]
            backtracking(index + 1)
            ans.pop()
            visited[i] = False
backtracking(0)
