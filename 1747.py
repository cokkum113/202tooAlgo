import sys
input = sys.stdin.readline

n = int(input())
def check(num):
    num = str(num)
    for i in range(1, len(num) // 2 + 1):
        if num[i - 1] != num[-i]:
            return False
    return True

def is_not_prime(x):
    for i in range (2, int(x**0.5) + 1):
        if x % i == 0:
            return True
    return False

ans = []
for i in range(int(10**7)):
    if check(i) and not is_not_prime(i):
        ans.append(i)

ans = ans[2:]
for i in ans:
    if i >= n:
        print(i)
        break
    