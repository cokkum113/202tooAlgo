import sys
input = sys.stdin.readline
from collections import deque

n, w, l = map(int, input().split())
# n은 다를 건너는 트럭의 수, w는 다리의 길이, l은 다리의 최대 하중

trucks = deque(list(map(int, input().split())))
bridge = deque([0] * w)
time = 0
arrived = 0


while True:
    if arrived == n:
        break

    if bridge:
        if bridge[0] != 0:
            arrived += 1
        bridge.popleft()
        # 공통된 것은 분기처리 하지 말고 빼기
    
    # 트럭에서 빼고 bridge에 올라갈 수 있는 경우와 아닌 경우로 나누면 분기 처리가 쉬워짐
    if trucks and trucks[0] + sum(bridge) <= l:
        x = trucks.popleft()
        bridge.append(x)
    else:
        # 올라갈 수 없는 경우에는 상관없는 값 0을 넣어준다.
        bridge.append(0)
        # 그래야 마지막까지 더해줄 수 있음
    # print(bridge)

    time += 1    
print(time)
    
