import sys
input = sys.stdin.readline

tree = {}
cnt = 0

while True:
    t = input().rstrip()

    if t == '':
        break
    else:
        if t in tree:
            tree[t] += 1
            cnt += 1
        else:
            tree[t] = 1
            cnt += 1

ans = sorted(tree.items())

for i in ans:
    print(i[0],"%.4f"%(i[1]*100/cnt), sep=' ')

