import sys
input = sys.stdin.readline

ans = []
def backtracking(index):
    if len(ans) == 6:
        print(*ans)
        return
    
    for i in range(index, len(num)):
        ans.append(num[i])
        backtracking(i + 1)
        ans.pop()

while True:
    x = list(map(int, input().split()))

    if len(x) == 1 and x[0] == 0:
        break

    if len(x) >= 2:
        k = x[0]
        num = x[1:]
        num.sort()
        backtracking(0)
    
    print()
