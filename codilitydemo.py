def solution(A):
    a = set(A)
    cnt = 1
    while cnt in a:
        cnt += 1
    return cnt