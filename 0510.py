def solution(s):
    answer = []
    s = s[2:-2]
    x = s.split('},{')
    dic = dict()
    for i, val in enumerate(x):
        dic[len(val)] = val
    
    dic = sorted(dic.items(), key = lambda x: x[0])
    ss = []
    for i in dic:
        x = i[1].split(',')
        ss.append(x)
        
    for i in ss:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
            
    return answer


