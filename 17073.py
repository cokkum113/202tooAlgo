import sys
input = sys.stdin.readline

# 하나 주고 -> 쌓아두고 -> 이것을 같이 하지 않을 것

# 부모노드에 물이 없을 때를 구하면 됨. ->
# 제일 리프노드랑 관련되어 있는 거같은데
# 루트노드가 아닌 리프노드 수로 20을 나누면?


u, v = map(int, input().split())

tree = [[] for _ in range(u + 1)]
for _ in range(u - 1):
    x, y = map(int, input().split())
    if x < y :
        tree[x].append(y)
    else:
        tree[y].append(x)

cnt = 0
for i in range(1, len(tree)):
    if len(tree[i]) == 0:
        cnt += 1

print(v/cnt)

