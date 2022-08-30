import sys
input = sys.stdin.readline

ss = input().rstrip()

s = ss.split('-')

nums = []
for i in s:
    if i.isdigit():
        nums.append(int(i))
    else:
        x = 0
        j = i.split('+')
        for jj in j:
            x += int(jj)
        nums.append(x)
            
ans = nums[0]
for i in range(1, len(nums)):
    ans -= nums[i]

print(ans)
        
