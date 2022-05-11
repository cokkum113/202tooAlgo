#방법 1. 백트래킹
def solution(n, data):
    total = 0
    answer = 0
    members = 8
    memlist = ['A', 'C', 'F', 'J', 'M', 'N', 'R', 'T']
    visited = [False] * members
    backtracking(0, visited, total, data, memlist, answer, n)
    return answer

def backtracking(index, visited, total, data, memlist, answer, n):
    if total == 8:
        answer += 1
        return answer
    for i in range(8):
        if visited[i] == False:
            visited[i] = True
            total += 1
            backtracking(index + 1,visited, total, data, memlist, answer, n)
            visited[i] = False
        # if check(data, memlist, n) == -1:
        #     return 0
        

def check(data, memlist, n):
    for i in range(n):
        number = data[i][-1]

        man1 = data[i][0]
        man2 = data[i][2]
        m1 = memlist.index(man1)
        m2 = memlist.index(man2)

        pos = data[i][-2]
        if pos == '=':
            if abs(m1 - m2) - 1 != number:
                return -1
            
        elif pos == '>':
            if abs(m1 - m2) - 1 <= number:
                return -1
            
        elif pos == '<':
            if abs(m1 - m2) -1 >= number:
                return -1
        
        
print(solution(2, ["N~F=0", "R~T>2"]))

'''

# 방법 2. 조합
from itertools import permutations
def solution(n, data):
    answer = 0
    memlist = ['A', 'C', 'F', 'J', 'M', 'N', 'R', 'T']
    mem = list(permutations(memlist, 8))
    for m in mem:
        for i in data:
            number = i[-1]

            man1 = i[0]
            man2 = i[2]
            m1 = m.index(man1)
            m2 = m.index(man2)

            pos = i[-2]
            if pos == '=':
                if abs(m1 - m2) - 1 != int(number):
                    answer += 1
                    break
            elif pos == '>':
                if abs(m1 - m2) - 1 <= int(number):
                    answer += 1
                    break
            elif pos == '<':
                if abs(m1 - m2) -1 >= int(number):
                    answer += 1
                    break
    return len(mem) - answer

print(solution(2, ["N~F=0", "R~T>2"]))
'''