import sys
input = sys.stdin.readline
import re

s = []
while True:
    s.extend(input().split())
    if s[-1] == 'E-N-D':
        break

maxi = 0
ans = ''
# re.sub("정규표현식", "변경하고 싶은 문자", "검색이 대상이 되는것")
s = [re.sub('[^a-z+-+]', '', x.lower()) for x in s]
s.sort(key=lambda x : -len(x))
print(s[0])