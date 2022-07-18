import sys
input = sys.stdin.readline
from collections import deque


t = int(input())
for _ in range(t):
    stack2 = deque()
    stack1 = input().rstrip()
    stack3 = deque()
    
    for i in range(len(stack1)):
        if stack1[i] == '>':
            if len(stack2) != 0:
                x = stack2.popleft()
                stack3.append(x)

        elif stack1[i] == '<':
            if len(stack3) != 0:
                x = stack3.pop()
                stack2.appendleft(x) 
        
        elif stack1[i] == '-':
            if len(stack3) != 0:
                stack3.pop()
        else:
            stack3.append(stack1[i])

    ans = stack3 + stack2
    print(''.join(map(str, ans)))
    
