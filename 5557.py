import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
nums = list(map(int, input().split()))

answer = nums[-1]
xx = nums[:-1]
cnt = 0
def backtracking(index, total):
    global cnt
    if index == len(xx):
        if total == answer:
            cnt += 1
    else:
        sum1 = total + xx[index]
        sum2 = total - xx[index]

        if 0 <= sum1 <= 20:
            backtracking(index + 1, sum1)
        if 0 <= sum2 <= 20:
            backtracking(index + 1, sum2)

backtracking(0, 0)
print(cnt)

# 백트래킹에서 시간초과가 나면
# dp로 답을 저장해나가는 방식으로 풀면 될거 같은데 ,,,,,,,