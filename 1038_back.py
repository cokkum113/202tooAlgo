import sys
input = sys.stdin.readline

cnt = 9
n = int(input())

def backtracking(index, limit, temp):
    global cnt

    if index == limit:
        cnt += 1

        if cnt == n:
            print(temp)
            exit()
    
    for i in range(int(temp[-1])):
        backtracking(index + 1, limit, temp + str(i))
    

if n < 10:
    print(n)
    exit()
else:
    for i in range(1, 11):
        for j in range(1, 10):
            backtracking(0, i, str(j))

print(-1)
    

