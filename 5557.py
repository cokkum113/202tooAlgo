import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
nums = list(map(int, input().split()))

ans = nums[-1]
numbers = nums[:-1]
cnt = 0
def backtracking(index, total):
    global cnt
    if index == n - 1:
        if total == ans:
            cnt += 1
        return
    else:
        sum_plus = total + numbers[index]
        sum_sub = total - numbers[index]

        if 0 <= sum_plus <= 20:
            backtracking(index + 1, sum_plus)
        if 0 <= sum_sub <= 20:
            backtracking(index + 1, sum_sub)

backtracking(0, 0)
print(cnt)