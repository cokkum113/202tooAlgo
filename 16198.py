import sys
input = sys.stdin.readline

n = int(input())
energy_list = list(map(int, input().split()))

maxi = 0

if n == 3:
    print(energy_list[0] * energy_list[2])
    exit() 

# 인덱스 (지금 어디 위치인지 나타내주는 index)
# 지금 있는 것의 현재 값
# 지금 있는 것의 배열
def backtracking(index, total, energy_list):
    global maxi
    if len(energy_list) == 3:
        maxi = max(maxi, total)
        return

    # 지금 있는 곳에서 할일
    if 0 < index < len(energy_list):
        total += (energy_list[index - 1] * energy_list[index + 1])
    
    # 다음으로 넘어가기
    for i in range(1, n):
        remember = total
        x = energy_list.pop(index)
        backtracking(i, total, energy_list)
        energy_list.insert(index, x)
        total = remember
    # 지금 있는 곳으로 돌아와서 할 일

backtracking(1, 0, energy_list)
print(maxi)


