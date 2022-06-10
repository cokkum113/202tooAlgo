import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n, s = map(int, input().split())

nums = list(map(int, input().split()))

ans = []
visited = [False] * (len(nums))
cnt = 0
def backtracking(index):
    global cnt
    if sum(ans) == s:
        cnt += 1
        return

    
    for i in range(index, len(nums)):
        ans.append(nums[i])
        visited[i] = True
        backtracking(i + 1)
        ans.pop()
        visited[i] = False
    
backtracking(0)
print(cnt)
