import sys
input = sys.stdin.readline

a, b = map(int, input().split())
matrix = []
for _ in range(a):
    matrix.append(list(map(int, input().split())))

# 이진수
b = bin(b)[2:]

# 항등행렬
identity_matrix = [[0] * a for _ in range(a)]
for i in range(a):
    for j in range(a):
        if i == j:
            identity_matrix[i][j] = 1

# 곱셈 함수
def multiple(A, B):
    result = [[0] * a for _ in range(a)]
    for i in range(a):
        for j in range(a):
            for k in range(a):
                result[i][j] += A[i][k] * B[k][j]
    
    for i in range(a):
        for j in range(a):
            result[i][j] %= 1000
    
    return result

# 2진법 자릿수만큼 제곱해주고, 제곱한 행렬끼리 곱해주면된다.
answer_matrix = identity_matrix
# b = b[::-1]
# for i in b:
#     if i == '1':
#         while i != 0:
for i in range(len(b)):
    if b[-i-1] == '1':
        while i != 0:
            matrix = multiple(matrix, matrix)
            i -= 1
        answer_matrix = multiple(answer_matrix, matrix)

for i in answer_matrix:
    print(*i)