#완주하지 못한 선수
def solution(participant, completion):
    answer = ""
    participant.sort()
    #최악의 경우_1000000
    completion.sort()
    #최악의 경우_99999
    completion += [""]
    # 1
    
    for i in range(len(participant)):
        #1000000
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    #대략적인 계산 : 200000 + 1 + 1000000 = 3000000 
    #1초가 안걸립니다.

#전화번호 목록
# 효율성 3, 4 실패
def solution(phone_book):
    answer = True
    for x in range(len(phone_book)):
        prefix = phone_book[x]
        #1000000 #들어오는 input 개수 최악일때
        #20 prefix 최악일때
    
        for i in phone_book:
            #1000000
            if prefix != i:
                new = i[:len(prefix)]
                if prefix == new:
                    return False
    return answer
    #10^12 + 20 = 약 1000초 걸립니다.

#위장
from collections import defaultdict
def solution(clothes):
    answer = 1
    l = defaultdict(int)
    for i in clothes:
        l[i[1]] += 1
        # 30

    
    for i in l:
        answer *= (l[i] + 1)
        #30
    return answer - 1

    #30 * 30 = 900
    #1초가 안걸립니다.


#전화번호 목록
def solution(phone_book):
    answer = True

    l = dict()
    for i in phone_book:
        l[i] = 0
    #최악의 경우 : 1000000
    
    for i in phone_book:
        # 1000000
        s = ""
        for j in i:
            #20
            s += j
            if s in l:
                #여기서는 곱하기가 아니라 더하기 why? 해시라서
                #1000000
                if s != i:
                    return False
    return answer

# 1000000 + 1000000 * 20 + 1000000 = 22000000 = 10^7
#1초가 안걸립니다. 대박...

#베스트앨범
from collections import defaultdict
def solution(genres, plays):
    answer = []
    pl = defaultdict(int)
    pl2 = {}
    for i in range(len(genres)):
        #100000
        p = plays[i]
        g = genres[i]
        if g in pl.keys():
            pl[g] += p
            pl2[g].append([p, i])
        else:
            pl[g] = p
            pl2[g] = [[p, i]]
            
    pl = sorted(pl.items(),key=lambda x : x[1],reverse=True)
    #100000
    
    for i in pl:
        #100000
        ans = pl2[i[0]]
        ans = sorted(ans, key=lambda x : x[0],reverse=True)
        cnt = 0
        for j in range(len(ans)):
            #99, 약 100
            if cnt == 2:
                break
            answer.append(ans[j][1])
            cnt += 1    
    return answer
    # 100000 + 100000 + 100000 * 100 = 10200000 = 10 ^ 7
  