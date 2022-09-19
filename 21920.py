import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

x = int(input())

total = 0
cnt = 0
def gcd(num, num2):
    if num2 == 0:
        return num
    return gcd(num2, num % num2)

for i in nums:
    maxi = max(i, x)
    mini = min(i, x)
    if gcd(maxi, mini) == 1:
        total += i
        cnt += 1

print(total//cnt)

