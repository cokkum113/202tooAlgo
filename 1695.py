from os import lseek
import re
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in range(1, len(nums)//2 + 1):
    if nums[i - 1] != nums[-i]:
        cnt += 1

print(cnt)