#모의고사
def solution(answers):
    answer = []
    ans1 = [1,2,3,4,5]
    ans2 = [2,1,2,3,2,4,2,5]
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    for i in range(len(answers)):
        #10000
        if answers[i] == ans1[(i) % 5]:
            cnt1 += 1
            #5
        if answers[i] == ans2[(i) % 8]:
            cnt2 += 1
            #8
        if answers[i] == ans3[(i) % 10]:
            cnt3 += 1
            #10
    
    s = max(cnt1, cnt2, cnt3)
    #3
    
    if cnt1 == s:
        answer.append(1)
    if cnt2 == s:
        answer.append(2)
    if cnt3 == s:
        answer.append(3)
        
    return answer
    # 10000*5*8*10 + 3
    
    
    #소수 찾기
from itertools import permutations
def solution(numbers):
    answer = 0
    a = []
    for i in numbers:
        a.append(i)
    b = []
    for i in range(1, len(a) + 1):
        s = list(permutations(a, i))
        b.append(s)
    c = []
    for i in b:
        #10^7
        for j in i:
            s = str(''.join(j))
            c.append(s)
    for i in range(len(c)):
        #10^7
        if c[i][0] == '0':
            c[i] = '0'
    c = list(set(c))
    cnt = 0
    
    nums = [True] * 9999999
    sqr = int(9999999 ** 0.5)
    for i in range(2, sqr + 1):
        #10^4
        if nums[i] == True:
            if nums[i] == True:
                for j in range(i + i,9999999, i):
                    #10^2
                    nums[j] = False
    for i in c:

        if nums[int(i)]== True and int(i) != 0 and int(i) != 1:
            cnt += 1
    
    return cnt

    #10^7 + 10^7 + 10^6


#카펫
def solution(brown, yellow):
    answer = []
    #2*x + 2*y = brown + 4
    a = brown + yellow
    for i in range(1, a + 1):
        #10^ 3 * 10 ^ 10^6
        if (a / i) % 1 == 0:
            x = a / i
            y = i
            if x >= y:
                if 2 * x + 2 * y == brown + 4:
                    answer = [x, y]
    return answer

    #10 ^9


        
       