import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()

maxi = 0
total = int(s[0])

def backtracking(index, total):
    global maxi
    if index == n:
        maxi = max(maxi, total)
        return

    if s[index] == '+':
        backtracking(index + 2, total + int(s[index + 1]))
        if index == n - 2:
            return
        #괄호시
        a = int(s[index + 1])
        b = int(s[index + 3])
        op = s[index + 2]

        if op == '+':
            backtracking(index + 4, total + (a + b))
        elif op == '-':
            backtracking(index + 4, total + (a - b))
        elif op == '*':
            backtracking(index + 4, total + (a * b))
    
    elif s[index] == '-':
        backtracking(index + 2, total - int(s[index + 1]))
        if index == n - 2:
            return
        
        a = int(s[index + 1])
        b = int(s[index + 3])
        op = s[index + 2]

        if op == '+':
            backtracking(index + 4, total - (a + b))
        elif op == '-':
            backtracking(index + 4, total - (a - b))
        elif op == '*':
            backtracking(index + 4, total - (a * b))
    
    elif s[index] == '*':
        backtracking(index + 2, int(s[index + 1]) * total)
        if index == n - 2:
            return
        
        a = int(s[index + 1])
        b = int(s[index + 3])
        op = s[index + 2]

        if op == '+':
            backtracking(index + 4, total * (a + b))
        elif op == '-':
            backtracking(index + 4, total * (a - b))
        elif op == '*':
            backtracking(index + 4, total * (a * b))

backtracking(1, total)
print(maxi)
