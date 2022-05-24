import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for _ in range(t):
    s = input()
    n = int(input())
    nums = input().rstrip()
    nums = nums[1:-1]
    nums = nums.split(',')
    nums = deque(nums)

    # print(len(nums))
    # deque는 빈배열도 1이었음,,,,,,,,
    # 대박.

    flag = 0
    even = 0

    if n == 0:
        nums = deque()

    for i in s:
        if i == 'R':
            even += 1
        elif i == 'D':
            if len(nums) == 0:
                flag = 1
                print('error')
                break
            else:
                if even % 2 == 0:
                    nums.popleft()
                else:
                    nums.pop()
    
    if flag == 0:
        if even % 2 == 0:
            print('[' + ','.join(nums) + ']')
        else:
            nums = list(nums)
            nums = nums[::-1]
            print('[' + ','.join(nums) + ']')
