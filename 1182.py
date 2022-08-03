import sys
input = sys.stdin.readline

n, s = map(int, input().split())

numlist = list(map(int, input().split()))

cnt = 0
def backtracking(index, total):
    global cnt

    if index == n:
        return
    
    total += numlist[index]

    if total == s:
        cnt += 1
    
    backtracking(index + 1, total)
    # 현재 numslist[index]를 선택했을 때

    backtracking(index + 1, total - numlist[index])
    # 현재 numslist[index]를 선택하지 않았을 때

backtracking(0, 0)
print(cnt)


