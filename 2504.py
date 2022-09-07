import sys
input = sys.stdin.readline

ss = input().rstrip()
st = []
ch = []

cnt1 = 0
cnt2 = 0

# for i in ss:
#     if i == '(':
#         cnt1 += 1

#     elif i == ')':
#         cnt1 -= 1

#     if i == '[':
#         cnt2 += 1
#     elif i == ']':
#         cnt2 -= 1
# if cnt1 != 0 or cnt2 != 0:
#     print(0)
#     exit()

for i in ss:
    if i == '(' or i == '[':
        ch.append(i)
    elif i == ']':
        if ch and ch[-1] == '[':
            ch.pop()
    elif i == ')':
        if ch and ch[-1] == '(':
            ch.pop()

if len(ch) != 0:
    print(0)
    exit()

for i in ss:
    if i == '(' or i == '[':
        st.append(i)
    
    elif i == ')':
        if st:
            if str(st[-1]).isdigit():
                total = 0
                for j in range(len(st) - 1, - 1, - 1):
                    if st[j] == '(':
                        st[j] = total * 2
                        break
                    else:
                        total += st[j]
                        st.pop()
            else:
                st.pop()
                st.append(2)

    elif i == ']':
        if st:
            if str(st[-1]).isdigit():
                total = 0
                for j in range(len(st) - 1, - 1, - 1):
                    if st[j] == '[':
                        st[j] = total * 3
                        break
                    else:
                        total += st[j]
                        st.pop()
            else:
                st.pop()
                st.append(3)

print(sum(st))
