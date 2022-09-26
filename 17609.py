import sys
input = sys.stdin.readline

# 회문 0
# 유사회문 1
# 그외 2


def p(s):
    for i in range(1, len(s)//2 + 1):
        if s[i - 1] != s[-i]:
            return False
    return True

def p2(s):
    flag = False
    lo = 0
    hi = len(s) - 1
    while lo < hi:
        if not flag and s[lo] == s[hi]:
            lo += 1
            hi -= 1
        elif not flag and s[lo] != s[hi]:
            flag = True
            lo += 1
        
        elif flag and s[lo] == s[hi]:
            lo += 1
            hi -= 1
        
        elif flag and s[lo] != s[hi]:
            return False
    return True
        
def p22(s):
    flag = False
    lo = 0
    hi = len(s) - 1
    while lo < hi:
        if not flag and s[lo] == s[hi]:
            lo += 1
            hi -= 1
        elif not flag and s[lo] != s[hi]:
            flag = True
            hi -= 1
        
        elif flag and s[lo] == s[hi]:
            lo += 1
            hi -= 1
        
        elif flag and s[lo] != s[hi]:
            return False
    return True
        

t = int(input())
for _ in range(t):
    s = input().rstrip()
    if p(s):
        print(0)
    else:
        if p2(s) or p22(s):
            print(1)
        else:
            print(2)


