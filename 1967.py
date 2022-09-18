import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
visited = [False] * (n + 1)
tree = [[] for _ in range(n + 1)]
weights = [0] * (n + 1)



for _ in range(n - 1):
    x, y, w = map(int, input().split())
    tree[x].append([y, w])
    tree[y].append([x, w])
    # 1. 인접리스트 1. 그래프 선택...
    # 다시 타고 들어갔다가 부모를 또 알기 위해 올라오는 상황이 있기 때문에
    # 모든 정보를 가지고 있도록 그래프를 선택.
    '''
    1. 인접리스트 - 1. 그래프, 2. 자식, 3. 부모
    2. 행렬 - 힙방식, 이진트리 트리, 값을 넣는 X

    '''
# 트리의 지름이란 
# 루트에서부터 제일 먼거 고르고, 거기서 다시 제일먼저 고르고.
# 거기서 제일 먼 노드를 구하면됨.


def dfs(x, weight, v):
    for y, w in tree[x]:
        if not v[y]:
            ss = w + weight
            v[y] = True
            weights[y] = ss
            dfs(y, ss, v)

visited[1] = True
dfs(1, 0, visited)
first_node = weights.index(max(weights))
visited2 = [False] * (n + 1)
visited2[first_node] = True
dfs(first_node, 0, visited2)
print(max(weights))
    