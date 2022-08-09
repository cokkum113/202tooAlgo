import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

cal = list(map(int, input().split()))

rr = 0
mini = int(1e9)
maxi = -int(1e9)

def backtrackcing(total, depth):
    global maxi, mini
    if depth == n - 1:
        maxi = max(maxi, total)
        mini = min(mini, total)
        return
    
    # 다음으로 갈 아이
    for i in range(4):
        rr = total
        if cal[i] == 0:
            continue
        elif cal[i] > 0:
            if i == 0:
                total += nums[depth + 1]
            elif i == 1:
                total -= nums[depth + 1]
            
            elif i == 2:
                total *= nums[depth + 1]
            else:
                if total < 0:
                    total = -1 * total
                    total //= nums[depth + 1]
                    total = -1 * total
                else:
                    total //= nums[depth + 1]
        cal[i] -= 1
        backtrackcing(total, depth + 1)
        cal[i] += 1
        total = rr

backtrackcing(nums[0], 0)
print(maxi)
print(mini)