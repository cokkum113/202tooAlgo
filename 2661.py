import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())

ans = []
endflag = 0
def backtracking(index):
    global ans
    global endflag

    if endflag == 1:
        exit()

    # 종료조건
    if len(ans) == n:
        endflag = 1
        print(*ans, sep='')
        return
    
    for i in range(1, 4):
        ans.append(i)
        if check(ans):
            backtracking(index + 1)
        ans.pop()


def check(aa):
    for i in range(1, len(aa)//2 + 1):
        for j in range(i, len(aa) - i + 1):
            if aa[j - i : j] == aa[j : i + j]:
                return False
    return True

backtracking(0)
