#체육복
def solution(n, lost, reserve):
    answer = 0
    answer = n - len(lost)
    
    lost.sort()
    reserve.sort()
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                answer += 1
                reserve[j] = -1
                lost[i] = -1

    aa = []
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j] + 1:
                aa.append(lost[i])
                reserve[j] = -1
                break
                
            elif lost[i] == reserve[j] - 1:
                aa.append(lost[i])
                reserve[j] = -1
                break
                
    aa = set(aa)
    
    answer += len(aa)    
    return answer

#탐욕법
def solution(name):
    
    cnt  = 0
    mini = len(name) - 1
    
    for i, val in enumerate(name):
        cnt += min(ord(val) - ord('A') , ord('Z') - ord(val) + 1)
        
        j = i + 1
        while j < len(name) and name[j] == 'A':
            j += 1
        
        mini = min(mini, 2 * i + len(name) - j, i + 2 * (len(name) - j))
    
    cnt += mini
    return cnt


#큰 수 만들기
from itertools import combinations
def solution(number, k):
    answer = ''
    a = []
    for i in number:
        while len(a) != 0 and a[-1] < i:
            if k > 0:
                a.pop()
                k -= 1
            else:
                break
        a.append(i)
    if k > 0:
        a = a[:-k]
    answer = ''.join(a)
    
    return answer