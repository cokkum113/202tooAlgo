import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

cnt = 0
n = int(input())

# 먼저 감소하는 숫자인지 판멸하는 함수
# 이거를 인덱스로 True면 카운트 증가시켜서 계속 진행
# 만약 False면 카운트는 그대로 가게하고 인덱스만 증가시킴

def check_decres(number):
    if len(str(number)) == 1:
        if number == 0:
            return False
        else:
            return True
    
    elif len(str(number)) > 1:
        xx = str(number)
        x = xx[0]
        for i in range(1, len(xx)):
            if int(xx[i]) >= int(x):
                return False
            elif int(xx[i]) < int(x):
                x = int(xx[i])
        return True

def backtracking(index):
    global cnt
    if n == cnt:
        return index
    
    for i in range(index, 1000001):
        if check_decres(i):
            cnt += 1
            backtracking(index + 1)
        else:
            backtracking(i + 1)

print(backtracking(0))