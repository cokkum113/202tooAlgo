import sys
input = sys.stdin.readline
from collections import deque


####################반례 찾을 수가 없습니다.!!!!!!!!!################
######질문 검색에 있는게 다 돌아감니다...##############


t = int(input())
for _ in range(t):
    s = input().rstrip()
    n = int(input())
    nums = input().rstrip()
    nums = nums[1:-1]
    nums = nums.split(',')
    nums = deque(nums)
   

    flag = 0
    ex = 0

    if n == 0:
        if s.count('D') > 0:
            print('error')
            ex = 1
            continue

    flag = 0
    ex = 0

    for i in s:
        if len(nums) == 0:
            if i == 'D':
                flag = 1
                ex = 1
                print('error')
                continue

        if flag == 1:
            if i == 'R':
                flag = 0
            elif i == 'D':
                if len(nums) != 0:
                    nums.pop()
                else:
                    ex = 1
                    print('error')
                    continue
        else:
            if i == 'R':
                flag = 1
            elif i == 'D':
                if len(nums) != 0:
                    nums.popleft()
                else:
                    ex = 1
                    print('error')
                    continue
    
    if flag == 1 and ex == 0:
        nums = list(nums)
        nums = nums[::-1]
        nums = deque(nums)
        
        sss = (','.join(nums))
        print('[' + sss + ']')

    elif flag == 0 and ex == 0:
        sss = (','.join(nums))
        print('[' + sss + ']')



# nums = list(nums)
# nums = nums[::-1]
# nums = deque(nums)


# 1
# RRDDDDDRRRRRDRDDDRRRRRDRRDRRRR
# 18
# [65,14,87,67,55,58,23,51,85,41,69,25,31,63,70,64,59,21]
# [70,63,31,25,69,41,85]