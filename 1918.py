import sys
input = sys.stdin.readline

s = input().rstrip()

st = [] # 잠깐 들려서 괄호다른거 처리하는 곳
ans = []

for i in s:
    if i.isalpha():
        ans.append(i)
    
    elif i == '(':
        st.append(i)
    elif i == '*' or i == '/':
        while st and (st[-1] == '*' or st[-1] == '/'):
            ans.append(st.pop())
        
        st.append(i)
    
    elif i == '+' or i == '-':
        while st and st[-1] != '(':
            ans.append(st.pop())
        st.append(i)
    
    elif i == ')':
        while st and st[-1] != '(':
            ans.append(st.pop())
        st.pop() # (를 빼는거, 짝꿍 빼는 거

# print(st)
st = st[::-1]
for i in st:
    ans.append(i)

print(''.join(ans))