import sys
input = sys.stdin.readline

n = int(input())
visited = [False] * (n + 1)
nums = []
def backtracking():
    if len(nums) == n:
        print(*nums)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            nums.append(i + 1)
            backtracking()
            visited[i] = False
            nums.pop()
backtracking()
