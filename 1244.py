from re import L
import sys
input = sys.stdin.readline

n = int(input())
light = list(map(int, input().split()))
light = [0] + light

def change_switch(switch_num):
    if light[switch_num] == 1:
        light[switch_num] = 0
    elif light[switch_num] == 0:
        light[switch_num] = 1

def boy_switch(switch_number):
    for i in range(switch_number, n + 1, switch_number):
        change_switch(i)

def girl_switch(switch_number):
    change_switch(switch_number)
    for i in range(n // 2):
        if switch_number - i < 1 or switch_number + i > n:
            break
        if light[switch_number - i] == light[switch_number + i]:
            change_switch(switch_number - i)
            change_switch(switch_number + i)
        else:
            break

s = int(input())
for _ in range(s):
    a, switch = map(int, input().split())
    if a == 1:
        boy_switch(switch)
    else:
        girl_switch(switch)

for i in range(1, n + 1):
    print(light[i], end=' ')
    if i % 20 == 0:
        print()

