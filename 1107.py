import sys
input = sys.stdin.readline


n = int(input())
m = int(input())

if m != 0:
    broken = list(map(int, input().split()))
elif n != 100 and m == 0:
    print(len(str(n)))
    exit(0)

diff = int(1e9)

diff = min(diff, abs(100 - n))
for i in range(500000 + 500001):
    nums = str(i)
    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break
        elif j == len(nums) - 1:
            diff = min(diff, abs(int(nums) - n) + len(nums))
print(diff)

    