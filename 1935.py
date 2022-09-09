import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

nums = []
for _ in range(n):
    nums.append(int(input()))

ll = []
for i in s:
    if i.isalpha():
        x = ord(i) - ord('A')
        ll.append(nums[x])
    else:
        n2 = ll.pop()
        n1 = ll.pop()

        if i == '+':
            ll.append(n1 + n2)
        
        elif i == '*':
            ll.append(n1 * n2)
        
        elif i == '-':
            ll.append(n1 - n2)
        else:
            ll.append(n1/n2)

print("%.2f"%ll[0])
