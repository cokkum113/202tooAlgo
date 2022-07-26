from audioop import mul
import sys
input = sys.stdin.readline

n, b = map(int, input().split())
b = bin(b)[2:]

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        matrix[i][j] %= 1000

def multiple(A, B):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    
    for i in range(n):
        for j in range(n):
            result[i][j] %= 1000
    return result

identity_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            identity_matrix[i][j] = 1

for i in b:
    if i == '1':
        identity_matrix=multiple(multiple(identity_matrix, identity_matrix), matrix)
    else:
        identity_matrix=multiple(identity_matrix, identity_matrix)

for i in identity_matrix:
    print(*i)