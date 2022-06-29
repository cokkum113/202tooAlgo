import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

cnt = 0
n = int(input())

if n == 0:
    print(0)
    exit()

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
flag = 0
for i in range(1, 1000001):
    if n == cnt:
        print(i - 1)
        exit()
        
    if check_decres(i):
        cnt += 1
    else:
        continue

print(-1)


    
