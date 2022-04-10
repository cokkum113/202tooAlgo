import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

belts = deque(list(map(int, input().split())))

robot_flag = deque(list(False for _ in range(2*n)))


def rotation(belts):
    x = belts.pop()
    belts.appendleft(x)
    y = robot_flag.pop()
    robot_flag.appendleft(y)

def robot_rotation(belts, robot_flag):
    for i in range(n - 2, -1, -1):
        if belts[i + 1] >= 1 and robot_flag[i] == True and robot_flag[i + 1] == False:
            robot_flag[i] = False
            robot_flag[i + 1] = True
            belts[i + 1] -= 1
        else:
            continue

def put_robot(belts, robot_flag):
    if belts[0] >= 1 and robot_flag[0] == False:
        belts[0] -= 1
        robot_flag[0] = True

def delet_robot(robot_flag):
    if robot_flag[n - 1] == True:
        robot_flag[n - 1] = False

ans = 0
while True:
    ans += 1

    rotation(belts)
    delet_robot(robot_flag)
    robot_rotation(belts, robot_flag)
    put_robot(belts, robot_flag)
    # delet_robot(robot_flag)

    if belts.count(0) >= k:
        break

print(ans)