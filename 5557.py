import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)


n = int(input())
nums = list(map(int, input().split()))

ans = nums[-1]
nums = nums[:-1]
cnt = 0
def backtracking(index, total):
    global cnt 
    if index == n - 1:
        if total == ans:
            cnt += 1
            return
    else:
        sum1 = total + nums[index]
        sum2 = total - nums[index]
        if 0 <= sum1 <= 20:
            backtracking(index + 1, sum1)
        if 0 <= sum2 <= 20:
            backtracking(index + 1, sum2)

backtracking(0, 0)
print(cnt)