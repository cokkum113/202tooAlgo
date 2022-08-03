import sys
input = sys.stdin.readline

def backtracking(index):
    if len(nums) == 6:
        print(*nums)
        return
    
    for i in range(n):
        if visited[i] == False:
            if nums and nums[-1] < xx[i] or len(nums) == 0:
                nums.append(xx[i])
                visited[i] = True
                backtracking(index + 1)
                nums.pop()
                visited[i] = False

while True:
    x = list(map(int, input().split()))
    n = x[0]
    nums = []
    if n == 0:
        break

    else:
        xx = x[1:]
        visited = [False] * n
        backtracking(0)
    
    print()