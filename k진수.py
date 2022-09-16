def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

    
def solution(n, k):
    answer = 0
    s = ''
    while n:
        s += str(n%k)
        n = n//k
    s = s[::-1]
    
    xx = list(map(int, filter(lambda x: x != '', s.split('0'))))
    
    for i in xx:
        if is_prime(i) == False and i != 1:
            answer += 1
    return answer