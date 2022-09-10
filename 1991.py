from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())

tree = defaultdict(list)

for _ in range(n):
    s = input().rstrip().split()

    tree[s[0]] = [s[1], s[2]]

def pre(start):
    if start == '.':
        return
    print(start,end='')
    pre(tree[start][0])
    pre(tree[start][1])

def inorder(v):
    if v == '.':
        return
    
    inorder(tree[v][0])
    print(v, end="")
    inorder(tree[v][1])

def post(v):
    if v == '.':
        return
    
    post(tree[v][0])
    post(tree[v][1])
    print(v,end='')

pre('A')
print()
inorder('A')
print()
post('A')