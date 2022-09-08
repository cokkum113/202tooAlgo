from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input().rstrip()
    n = int(input())
    nums = input().rstrip()
    flag = False
    flag2 = False
    for i in s:
        if i == 'D':
            flag2 = True
            break
    
    if n == 0:
        if not flag2:
            print([])
            continue
        elif flag2:
            print('error')
            continue
    else:
        nums = nums[1:-1]
        nums = nums.split(',')
        nums = deque(nums)

        rcnt = 0
        for i in s:
            if i == 'R':
                rcnt += 1
            
            elif i == 'D':
                if nums:
                    if rcnt % 2 == 0:
                        nums.popleft()
                    else:
                        nums.pop()
                else:
                    flag = True
                    break
                    
        if flag:
            print('error')
        else:
            if rcnt % 2 == 0:
                print("[", end="")
                print(",".join(nums), "]", sep='')
            else:
                nums = list(nums)
                nums = nums[::-1]
                print("[", end="")
                print(",".join(nums), "]", sep='')

             
        


