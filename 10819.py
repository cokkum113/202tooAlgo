import sys
input = sys.stdin.readline

n = int(input())
total = []
answer = 0
maxi = 0
nums = list(map(int, input().split()))
visited = [False] * n

def backtracking(index):
    global maxi
    if len(total) == n:
        answer = 0
        for i in range(1, len(total)):
            answer += abs(total[i - 1] - total[i])
        maxi = max(maxi, answer)
    for i in range(n):
        if visited[i] == False:
            total.append(nums[i])
            visited[i] = True
            backtracking(index + 1)
            visited[i] = False
            total.pop()
    
backtracking(0)
print(maxi)