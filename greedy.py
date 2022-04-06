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

#구명보트
def solution(people, limit):
    cnt = 0
    st = 0
    end = len(people) - 1
    people.sort()
    while st <= end:
        cnt += 1
        if people[st] + people[end] <= limit:
            st += 1
        
        end -= 1
    return cnt

#섬 연결하기 ######유니온파인드 질문
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x : x[2])
    parent = [i for i in range(n)]
    for a, b, cost in costs:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost
    
    
    return answer
def find(parent, n):
    if parent[n] != n:
        parent[n] = find(parent, parent[n])
    return parent[n]

def union(parent, a, b):
    rootA = parent[a]
    rootB = parent[b]
    parent[rootA] = rootB


#단속카메라
def solution(routes):
    answer = 0
    routes.sort(key=lambda x : x[1])
    cam = routes[0][1]
    answer = 1
    for i in range(1, len(routes)):
        if cam < routes[i][0]:
            cam = routes[i][1]
            answer += 1
        else:
            continue
            
    return answer