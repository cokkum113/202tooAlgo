import sys
input = sys.stdin.readline
from collections import deque

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

'''
graph = [[-1] * w for _ in range(h)]
visited = [[False] * w for _ in range(h)]

blocks = list(map(int, input().split()))

new_graph = []
for i in range(w):
    new_list = list(zip(*graph))[i]
    new_list = list(new_list)
    for j in range(blocks[i]):
        new_list[j] = 0
    new_graph.append(new_list)

ans_graph = []
for i in range(h):
    new_list = list(zip(*new_graph))[i]
    new_list = list(new_list)
    
    ans_graph.append(new_list)

ans_graph = ans_graph[::-1]

# 0이 block
'''

ans = 0
for i in range(1, w - 1):
    max_left = max(blocks[: i + 1])
    max_right = max(blocks[i:])
    mini = min(max_left, max_right)
    ans += abs(blocks[i] - mini)

print(ans)
