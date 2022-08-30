from collections import deque
def solution(queue1, queue2):
    answer = -1
    q1 = deque(queue1)
    q2 = deque(queue2)
    t1 = sum(queue1)
    t2 = sum(queue2)
    
    maxi = max(len(queue1), len(queue2))
    
    for i in range(maxi * 100):
        if t1 == t2:
            return i
        if t1 > t2:
            xx = q1.popleft()
            q2.append(xx)
            t1 -= xx
            t2 += xx
        elif t1 < t2:
            xx = q2.popleft()
            q1.append(xx)
            t2 -= xx
            t1 += xx
    return -1
            
            
    