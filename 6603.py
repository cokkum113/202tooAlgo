import sys
input = sys.stdin.readline

#k개의 수를 골라 집합을 만들고 그 수만 가지고 번호를 선택하는 것
# 그러고 여기서 고를 수 있는 경우의 수를 구하기

    
ans = []
def backtracking(index):
    if len(ans) == 6:
        print(*ans)
        return
    
    for i in range(index, len(nums)):
        ans.append(nums[i])
        visited[nums[i]] = True
        backtracking(i + 1)
        ans.pop()
        visited[nums[i]] = False

while True:
    x = list(map(int, input().split()))

    if len(x) == 1 and x[0] == 0:
        break
    
    if len(x) >= 2:
        k = x[0]
        nums = x[1:]
        nums.sort()
        visited = [False] * 50
        backtracking(0)
    
    print()

    

