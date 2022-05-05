#연습문제 124나라의 숫자
def solution(n):
    answer = ''
    world124 = [1, 2, 4]
    
    while n > 0:
        n -= 1
        #이 n-=1을 먼저 꼭 해야함!!! 0부터 시작하니까!!
        answer = str(world124[n%3]) + answer
        n //= 3
    return answer

