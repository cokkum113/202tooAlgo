from itertools import permutations
import sys
input = sys.stdin.readline
#person = [i for i in range(1, 10)]
#1번은 정해져 있어서 2번부터 돌리면됨
person = [i for i in range(1, 9)]
pp = list(permutations(person, 8))
#이 순서로 1번을 무시하고 만들면됨
n = int(input())
res = []
for _ in range(n):
    res.append(list(map(int, input().split())))
    
maxi = 0
for i in pp:
    score = 0
    ll = list(i)
    li = ll[:3] + [0] + ll[3:]

    idx = 0

    for j in range(n):
        out = 0
        b1 = 0
        b2 = 0
        b3 = 0
        while out < 3:
            if res[j][li[idx]] == 0:
                out += 1
            elif res[j][li[idx]] == 1:
                score += b3
                b3 = b2
                b2 = b1
                b1 = 1
            elif res[j][li[idx]] == 2:
                score += b3 + b2
                b3 = b1
                b2 = 1
                b1 = 0
            elif res[j][li[idx]] == 3:
                score += b3 + b2 + b1
                b3 = 1
                b2 = 0
                b1 = 0
            elif res[j][li[idx]] == 4:
                score += b3 + b2 + b1 + 1
                b3 = 0
                b2 = 0
                b1 = 0
            
            idx += 1

            if idx == 9:
                idx = 0
    
    maxi = max(maxi, score)
  
print(maxi)