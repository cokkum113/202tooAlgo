import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())

answers = []

for i in range(1, 11):
    for combi in combinations(range(0, 10), i):
        xx = list(combi)
        xx.sort(reverse=True)
        answers.append(int(''.join(map(str, xx))))

answers.sort()
try:
    print(answers[n])
except:
    print(-1)