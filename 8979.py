import sys
input = sys.stdin.readline

# 금메달 수가 더 많은 나라
# 은메달 수가 더 많은나라
# 동메달 수가 더 많은 나라

n, k = map(int, input().split())
nlist = []
for _ in range(n):
    na, g, s, b = input().rstrip().split()
    nlist.append([int(g), int(s), int(b), int(na)])

nlist.sort(key = lambda x : (-x[0], -x[1], -x[2]))

cnt = 0
ng = 0
ns = 0
same = 0
nb = 0
flag = True
for i in nlist:
    g, s, b, na = i[0], i[1], i[2], i[3]
    if ng != g or ns != s or nb != b:
        if same != 0:
            cnt += same
            same = 0
        cnt += 1
        ng = g
        nb = b
        ns = s
    else:
        same += 1


    if na == k:
        break
print(cnt)

