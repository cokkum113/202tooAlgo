from collections import defaultdict
def solution(survey, choices):
    answer = ''
    ll = defaultdict(int)
    ll['R'] = 0
    ll['T'] = 0
    ll['C'] = 0
    ll['F'] = 0
    ll['J'] = 0
    ll['M'] = 0
    ll['A'] = 0
    ll['N'] = 0
    
    for i in range(len(survey)):
        x = survey[i][0]
        y = survey[i][1]
        if choices[i] == 1 or choices[i] == 2 or choices[i] == 3:
            if choices[i] == 1:
                ll[x] += 3
            elif choices[i] == 2:
                ll[x] += 2
            elif choices[i] == 3:
                ll[x] += 1
        elif choices[i] == 5 or choices[i] == 6 or choices[i] == 7:
            if choices[i] == 7:
                ll[y] += 3
            elif choices[i] == 6:
                ll[y] += 2
            elif choices[i] == 5:
                ll[y] += 1
        
    if ll['R'] > ll['T']:
        answer += 'R'
    elif ll['R'] < ll['T']:
        answer += 'T'
    elif ll['R'] == ll['T']:
        answer += 'R'
    
    
    if ll['C'] > ll['F']:
        answer += 'C'
    elif ll['C'] < ll['F']:
        answer += 'F'
    elif ll['C'] == ll['F']:
        answer += 'C'
        
    
    if ll['J'] > ll['M']:
        answer += 'J'
    elif ll['J'] < ll['M']:
        answer += 'M'
    elif ll['J'] == ll['M']:
        answer += 'J'
    
    if ll['A'] > ll['N']:
        answer += 'A'
    elif ll['A'] < ll['N']:
        answer += 'N'
    elif ll['A'] == ll['N']:
        answer += 'A'
    
    
    return answer