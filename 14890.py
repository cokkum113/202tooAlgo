import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

def all_same(one_line):
    for i in range(len(one_line) - 1):
        if one_line[i] != one_line[i + 1]:
            return False
    return True

    
def line_check(one_line):
    visit = [False] * n
    for i in range(0, len(one_line) - 1):
        if abs(one_line[i] - one_line[i + 1]) == 1:
            if one_line[i] > one_line[i + 1]: 
                for j in range(i + 1, i + 1 + l):
                    if 0 <= j < n:
                        if one_line[i + 1] != one_line[j]: 
                            return False
                        if visit[j] == True: 
                            return False
                        visit[j] = True
                    else:
                        return False
                    
            elif one_line[i] < one_line[i + 1]:
                for j in range(i, i - l, -1):
                    if 0 <= j < n:
                        if one_line[i] != one_line[j]: 
                            return False
                        if visit[j] == True: 
                            return False
                        visit[j] = True
                    else:
                        return False

        elif abs(one_line[i] - one_line[i + 1]) > 1: 
            return False
    return True



cnt = 0
for i in graph:
    if line_check(i) or all_same(i):
        cnt += 1

new_graph = list(zip(*graph))
for i in new_graph:
    if line_check(i) or all_same(i):
        cnt += 1

print(cnt)