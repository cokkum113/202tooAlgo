import sys
input = sys.stdin.readline

t = int(input())

def one(s, st, end):
    while st < end:
        if s[st] == s[end]:
            st += 1
            end -= 1
        else:
            return 2
    return 1

def zero(s, st, end):
    while st < end:
        if s[st] == s[end]:
            st += 1
            end -= 1
        else:
            new_s1 = one(s, st + 1, end)
            new_s2 = one(s, st, end -1)
            if (new_s1 == 1 and new_s2 == 2) or (new_s1 == 2 and new_s2 == 1) or (new_s1 == 1 and new_s2 == 1):
                return 1
            else:
                return 2
    return 0


for _ in range(t):
    s = input().rstrip()
    print(zero(s, 0, len(s) - 1))
