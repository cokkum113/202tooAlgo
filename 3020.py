import sys
input = sys.stdin.readline

n, h = map(int, input().split())


seok = []
jong = []
for i in range(n):
    if i % 2 == 0:
        seok.append(int(input()))
    else:
        jong.append(int(input()))

seok.sort()
jong.sort()

mini = n
mini_cnt = 0

def binary(arr, target, st, end):
    while st <= end:
        mid = (st + end) // 2

        if arr[mid] < target:
            st = mid + 1
        elif arr[mid] >= target:
            end = mid - 1
    
    return st


for i in range(1, h + 1):
    seok_cnt = len(seok) - binary(seok, i - 0.5, 0 , len(seok) - 1)
    jong_cnt = len(jong) - binary(jong, h - i + 0.5, 0, len(jong) - 1)

    if mini == seok_cnt + jong_cnt:
        mini_cnt += 1

    elif mini > seok_cnt + jong_cnt:
        mini_cnt = 1
        mini = seok_cnt + jong_cnt

print(mini, mini_cnt)

