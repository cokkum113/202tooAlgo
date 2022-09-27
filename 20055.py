import sys
input = sys.stdin.readline
from collections import deque

def step1(que1):
    que1.appendleft(que1.pop())

def step2(que1, n):
    for i in range(n - 2, -1, -1):
        if que1[i + 1][0] >= 1 and que1[i][1] == 1 and que1[i + 1][1] == 0:
            que1[i + 1][0] -= 1
            que1[i][1] = 0
            que1[i + 1][1] = 1
        else:
            continue
    
def put(que1):
    if que1[0][0] >= 1 and que1[0][1] == 0:
        que1[0][1] = 1
        que1[0][0] -= 1
def delete(que1, n):
    if que1[n - 1][1] == 1:
        que1[n - 1][1] = 0

n, k = map(int, input().split())
cnt = 0
ll = list(map(int, input().split()))

que = deque()
for i in ll:
    que.append([i, 0])

while True:
    cnt += 1
    
    step1(que)
    delete(que, n)
    step2(que, n)
    put(que)
    delete(que, n)

    zero = 0
    for i in que:
        if i[0] == 0:
            zero += 1
    if zero >= k:
        break

    
print(cnt)

