import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
visited = [False] * n
op = list(map(int, input().split()))

mini = int(1e9)
maxi = -int(1e9)

re = 0

def backtracking(index, total):
    global mini, maxi
    if index == n - 1:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return
    
    for i in range(4):
        re = total
        if op[i] == 0:
            continue
        else:
            if i == 0:
                total += nums[index + 1]
            elif i == 1:
                total -= nums[index + 1]
            elif i == 2:
                total *= nums[index + 1]
            else:
                if total < 0:
                    total = -1 * total // nums[index + 1]
                    total = -1 * total
                else:
                    total //= nums[index + 1]
        
        op[i] -= 1
        backtracking(index + 1, total)
        op[i] += 1
        total = re

backtracking(0, nums[0])
print(maxi)
print(mini)
            

