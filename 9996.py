# import sys
# input = sys.stdin.readline

# n = int(input())
# pattern = input().rstrip()

# p = pattern.split('*')
# pp = ''.join(p)
# for _ in range(n):
#     s = input().rstrip()
#     s1 = s[:len(p[0])]
#     s2 = s[-len(p[1]):]

#     if s1 == p[0] and s2 == p[1] and len(s) >= len(pp):
#         print("DA")
#     else:
#         print("NE")


# import re
# i=input
# T,p=int(i()),i().replace("*",".*")+"$"
# exec('print("DA"if re.match(p,i())else"NE");'*T)

import re
n = int(input())
p = input().replace("*", ".*")+"$"
exec('print("DA" if re.match(p, input().rstrip())else "NE");'*n)

