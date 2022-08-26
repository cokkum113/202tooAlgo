import sys
input = sys.stdin.readline

n = int(input())
if n <= 9:
    print(n)
    exit()

cnt = 9

def backtracking(index, limit, nums):
    global cnt
    if index == limit:
        cnt += 1
        if cnt == n:
            print(nums)
            exit()
    
    for i in range(int(nums[-1])):
        backtracking(index + 1, limit, nums + str(i))

for i in range(1, 11):
    for j in range(1, 10):
        backtracking(0, i, str(j))
print(-1)