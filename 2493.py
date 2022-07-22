import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))

ans = [0] * n
# 뒤에 더 큰게 나타나면 쓸모가 없어짐
stack = []

# def check(stack, now_pos):
#     for i in range(len(stack)-1, -1, -1):
#         if now_pos < stack[i][1]:
#             return stack[i][0]

for i in range(n):
    if not stack:
        ans[i] = 0
    # else:
    #     if stack[-1][1] >= top[i]:
    #         ans[i] = stack[-1][0]
    #     else:
            # 이 부분 처리가 결국 시간초과나는 코드 for문안에서 결국
            # for문을 돌게됨

            # if check(stack, top[i]):
            #     ans[i] = check(stack, top[i])
            # else:
            #     ans[i] = 0
            # stack.pop()
    # 스택안에서만 돌게 하면됨

    while stack:
        if stack[-1][1] >= top[i]:
            ans[i] = stack[-1][0]
            break
        else:
            stack.pop()
    stack.append([i + 1, top[i]])


print(' '.join(map(str,(ans))))