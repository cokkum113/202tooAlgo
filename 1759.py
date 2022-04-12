import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
ans = []

must1 = ['a', 'e', 'i','o','u']
must2 = ['b', 'c', 'd','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

L, C = map(int, input().split())
alpha = list(map(str, input().split()))

alpha.sort()
visited = [False] * C
def backtracking(start):
    if len(ans) == L:
        mu1 = 0
        mu2 = 0
        for i in ans:
            if i in must1:
                mu1 += 1
            if i in must2:
                mu2 += 1
        if mu1 >= 1 and mu2 >= 2:
            print(''.join(ans))
            return

    for i in range(len(alpha)):
        if visited[i]:
            continue
        visited[i] = True
        ans.append(alpha[i])
        backtracking(i)
        ans.pop()
        for j in range(i + 1, len(alpha)):
            visited[j] = False    

backtracking(0)