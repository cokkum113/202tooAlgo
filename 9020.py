import sys
input = sys.stdin.readline

primelist = []
def prime(n):
    nums = [True] * n
    sqr = int(n ** 0.5)

    nums[0] = False
    nums[1] = False

    for i in range(2, sqr + 1):
        if nums[i]:
            for j in range(i + i, n, i):
                nums[j] = False
    
    for i in range(len(nums)):
        if nums[i]:
            primelist.append(i)
    return primelist


t = int(input())
for _ in range(t):
    primelist = []
    n = int(input())
    prime(n)
    anslist = []
    
    p = primelist
    for i in p:
        for j in p:
            if i + j == n:
                anslist.append([i, j])
    mini = 10001
    for i in range(len(anslist)//2 + 1):
        if abs(anslist[i][0] - anslist[i][1]) < mini:
            mini = abs(anslist[i][0] - anslist[i][1])
            ans1 = anslist[i][0]
            ans2 = anslist[i][1]
    
    print(ans1, ans2)

    
        