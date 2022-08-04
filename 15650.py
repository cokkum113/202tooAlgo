import sys
input = sys.stdin.readline

n, m = map(int, input().split())

nums = []
visited = [False] * (n + 1)

def backtracking(index):
    if len(nums) == m:
        print(*nums)
        return
    
    for i in range(1, n + 1):
        if visited[i] == False:
            if nums and nums[-1] < i or len(nums) == 0:
                nums.append(i)
                visited[i] = True
                backtracking(index + 1)
                visited[i] = False
                nums.pop()

backtracking(0)
            


