import sys
input = sys.stdin.readline

#비내림차순은 같을수 있음

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
visited = [False] * (n + 1)
ans = []

def backtracking(index):

    if len(ans) == m:
        print(*ans)
        return
    
    for i in range(1, n + 1):
        if visited[i - 1] == False:
            ans.append(nums[i - 1])
            visited[i] = True
            backtracking(index + 1)
            ans.pop()
            visited[i] = False
            visited[i - 1] = True
        

backtracking(0)