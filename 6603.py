import sys
input = sys.stdin.readline

def backtracking(index):
    if len(nums) == 6:
        print(nums)
        return
    
    for i in range(index, 7):
        if visited[i]:
            continue
        visited[i] = True
        nums.append(xlist[i])
        backtracking(index + 1)
        visited[i] = False
        nums.pop()
    

while True:
    x = list(map(int, input().split()))
    if x[0] == 0:
        break
    n = x[0]
    xlist = x[1:]

    nums = []
    visited = [False] * n

    backtracking(0)

    print()