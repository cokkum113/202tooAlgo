import sys
input = sys.stdin.readline
from collections import deque

st1 = deque(list(input().rstrip()))
st2 = deque()

n = int(input())

# 스택!으로 푸는 문제.
# 커서를 어떻게 움직일 것인지가 중요!!
# 이건 스택이 두개면 된다!!!! 유레카...
# L을 할때마다 스택을 다른 곳으로 옮기고 
# 마지막에 하나는 스택을 반대로 나오게 하면된다. 

# 스택말고 deque를 쓰는 방법이 있음

order = []
# flag = False
for _ in range(n):
    m = input().split()
    order.append(m)

#플래그까지가 필요없음
for o in order:
    if o[0] == 'L':
        if len(st1) != 0 and len(st2) == 0:
            x = st1.pop()
            st2.appendleft(x)
        elif len(st1) != 0 and len(st2) != 0:
            x = st1.pop()
            st2.appendleft(x)
    
    elif o[0] == 'D':
        if len(st1) == 0 and len(st2) != 0:
            x = st2.popleft()
            st1.append(x)
        
        elif len(st1) != 0 and len(st2) != 0:
            x = st2.popleft()
            st1.append(x)
        
        

    elif o[0] == 'B':
        if len(st1) != 0 and len(st2) == 0:
            st1.pop()
        elif len(st1) != 0 and len(st2) != 0:
            st1.pop()


    elif o[0] == 'P':
        if len(st1) == 0 and len(st2) != 0:
            st1.append(o[1])
        elif len(st1) != 0 and len(st2) == 0:
            st1.append(o[1])
        elif len(st1) != 0 and len(st2) != 0:
            st1.append(o[1])
        elif len(st1) == 0 and len(st2) == 0:
            st1.append(o[1])
                
        

    # print('--------------')  
    # print(st1)
    # print('########')
    # print(st2)
    # print('--------------')  

ans = list(st1) + list(st2)
print(''.join(ans))
