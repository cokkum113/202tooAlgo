import sys
input = sys.stdin.readline

n, m = map(int, input().split())
xlist = list(map(int, input().split()))

visited = [False] * n

xlist.sort()

nums = []

def backtracking(index):
    if len(nums) == m:
        # print(*nums)
        return
    x = 0
    for i in range(n):
        if visited[i] == False and x != xlist[i]:
            print(x, xlist[i])
            if nums and nums[-1] <= xlist[i] or not nums:
                nums.append(xlist[i])
                visited[i] = True
                x = xlist[i]
                print(x)
                backtracking(index + 1)
                visited[i] = False
                nums.pop()
backtracking(0)

