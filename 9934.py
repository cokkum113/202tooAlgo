import sys
input = sys.stdin.readline

h = int(input())
nodes = list(map(int, input().split()))

n = 2**h - 1

tree = [[] for _ in range(h)]

# 중위순회방식
def inorder(index, left, right):
    if index == h:
        return
    
    root = (right - left) // 2 + left
    tree[index].append(nodes[root])
    inorder(index + 1, left, root - 1)
    inorder(index + 1, root + 1, right)

inorder(0, 0, n)
for i in tree:
    print(*i)