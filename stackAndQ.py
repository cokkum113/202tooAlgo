#기능개발
def solution(progresses, speeds):
    answer = []
    stack = []
    for i in range(len(progresses)):
        #100
        y = (100 - progresses[i]) *100 / (speeds[i]) 
        #이 부분 때문인거같은데...수정하면 2번이 틀리고, 수정하면 11번이 틀림
        # y = (100 - progresses[i]) // (speeds[i]) 
        stack.append(y)
        
    big = stack[0]
    cnt = 1
    
    for i in range(1, len(stack)):
        #100
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
######  200 : 1초가 안됨

#프린터
from collections import deque
def solution(priorities, location):
    answer = 0
    maxi = max(priorities)
    
    p = deque()
    for i, val in enumerate(priorities):
        p.append([val, i])
        #100
    
    cnt = 1
    while True:
        x = p.popleft()
        #100
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
    ### 200 _ 1초가 안됨

#주식가격
def solution(prices):
    answer = []
    for i in range(len(prices)):
        #10000
        cnt = 0
        for j in range(i + 1, len(prices)):
            #10000
            if prices[i] > prices[j]:
                cnt += 1
                break
            else:
                cnt += 1
        answer.append(cnt)
    return answer
    ##### 10^8 _ 1초가 안됨

#다리건너기
from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck = deque(truck_weights)
    cnt = 0
    to = 0
    
    while len(bridge) != 0:
        
        cnt += 1
        to -= bridge.popleft()
        #sum을 쓰면 시초뜨게 됨 10000를 for문 안에서 돌리게 돼서
        #10000
        if len(truck) != 0:
            if truck[0] + to <= weight:
                x = truck.popleft()
                #10000
                bridge.append(x)
                to += x
            else:
                bridge.append(0)
                    
    return cnt
    #10^8 _ 1초가 안됨

