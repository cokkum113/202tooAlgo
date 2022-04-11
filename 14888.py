import sys
input = sys.stdin.readline

mini = int(1e9)
maxi = -int(1e9)

n = int(input())

nums = list(map(int, input().split()))
cal = list(map(int, input().split()))

def backtracking(index, cur): 
    global mini 
    global maxi 
    if index == n-1: 
        if mini >= cur: 
            mini = cur 
        if maxi <= cur: 
            maxi = cur 
        return cur 

    for i in range(4): 
        remember = cur 
        if cal[i]==0: 
            continue 
        elif cal[i] >= 1:
            if i == 0: 
                cur += nums[index + 1] 
            elif i == 1: 
                cur -= nums[index + 1]
            elif i==2: 
                cur *= nums[index + 1] 
            else: 
                if cur < 0: 
                    cur = -1*cur // nums[index + 1]* - 1 
                else: 
                    cur //= nums[index + 1] 
            
        cal[i] -= 1 
        backtracking(index + 1, cur) 
        cal[i] += 1 
        cur = remember 


backtracking(0, nums[0])
print(maxi)
print(mini)
