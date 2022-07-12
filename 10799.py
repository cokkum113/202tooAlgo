import sys
input = sys.stdin.readline

s = input().rstrip()

# stick = []
stick_cnt = 0
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        # stick.append('(')
        stick_cnt += 1
    else:
        if s[i - 1] == '(':
            stick_cnt -= 1
            #레이저여서 빼준 것
            ans += stick_cnt
        else:
            stick_cnt -=1
            ans += 1
print(ans)

        