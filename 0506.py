def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    stack = []
    for i in s:
        x = i.split(',')
        stack.append(x)
        
    stack.sort(key = lambda x : len(x))
    for i in stack:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))
        
    return answer


def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                answer += 1
                lost[i] = -1
                reserve[j] = -1
    # print(reserve)
    # print(lost)
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] + 1 == reserve[j]:
                answer += 1
                reserve[j] = -1
                break
            elif lost[i] - 1 == reserve[j]:
                answer += 1
                reserve[j] = -1
                break
    return answer
                
from collections import deque
def solution(numbers, target):
    answer = 0
    que = deque()
    que.append([-numbers[0], 0])
    que.append([numbers[0], 0])
    
    while que:
        x, index = que.popleft()
        if index == len(numbers) - 1:
            if x == target:
                answer += 1
        else:
            index += 1
            que.append([x + numbers[index], index])
            que.append([x - numbers[index], index])
    return answer

def solution(answers):
    answer = []
    ans1 = [1,2,3,4,5]
    ans2 = [2,1,2,3,2,4,2,5]
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    for i in range(len(answers)):
        if answers[i] == ans1[(i) % 5]:
            cnt1 += 1
        if answers[i] == ans2[(i) % 8]:
            cnt2 += 1
        if answers[i] == ans3[(i) % 10]:
            cnt3 += 1
    
    s = max(cnt1, cnt2, cnt3)
    
    if cnt1 == s:
        answer.append(1)
    if cnt2 == s:
        answer.append(2)
    if cnt3 == s:
        answer.append(3)
        
    return answer

def solution(answers):
    answer = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    giveup = [0, 0, 0]
    # print(answers)
    for i in range(len(answers)):
        if a1[i%(len(a1))] == answers[i]:
            giveup[0] += 1
        if a2[i % len(a2)] == answers[i]:
            giveup[1] += 1
        if a3[i % len(a3)] == answers[i]:
            giveup[2] += 1
    for i, val in enumerate(giveup):
        if val == max(giveup):
            answer.append(i + 1)
    return answer