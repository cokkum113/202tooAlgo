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