#기능개발
def solution(progresses, speeds):
    answer = []
    stack = []
    for i in range(len(progresses)):
        y = (100 - progresses[i]) *100 / (speeds[i]) 
        #이 부분 때문인거같은데...수정하면 2번이 틀리고, 수정하면 11번이 틀림
        # y = (100 - progresses[i]) // (speeds[i]) 
        stack.append(y)
        
    big = stack[0]
    cnt = 1
    
    for i in range(1, len(stack)):
        if big < stack[i]:
            big = stack[i]
            answer.append(cnt) 
            cnt = 1       
        else:
            cnt += 1

        if i == len(stack) - 1:
            answer.append(cnt) 
    return answer


#기능개발 맞은 것!!!
import math
def solution(progresses, speeds):
    answer = []
    stack = []
    for i in range(len(progresses)):
        y = (100 - progresses[i]) / speeds[i]
        y = math.ceil(y)
        #y = round(y, 3982984) 안되고 , ceil해서 다 올리니까 통과!!! 오예 ㅠㅠㅠ
        stack.append(y)
        
    big = stack[0]
    cnt = 1
    
    for i in range(1, len(stack)):
        if big < stack[i]:
            big = stack[i]
            answer.append(cnt) 
            cnt = 1       
        else:
            cnt += 1

        if i == len(stack) - 1:
            answer.append(cnt) 
    return answer

#프린터
from collections import deque
def solution(priorities, location):
    answer = 0
    maxi = max(priorities)
    
    p = deque()
    for i, val in enumerate(priorities):
        p.append([val, i])
    
    cnt = 1
    while True:
        x = p.popleft()
        if x[0] == maxi:
            if x[1] == location:
                return cnt
            else:
                cnt += 1
                maxi = max(p)[0]

        elif x[0] < maxi:
            p.append(x)

    answer = cnt
    return answer

#주식가격
def solution(prices):
    answer = []
    a = len(prices)
    lo = prices[0]
    cnt = 0
    
    for i in range(1, len(prices)):
        if lo < prices[i]:
            if cnt == 0:
                ans = a - i
                answer.append(ans)
                lo = prices[i]
            else:
                ans = cnt
                answer.append(ans)
                cnt = 0
        elif lo > prices[i]:
            cnt += 1
            
    return answer