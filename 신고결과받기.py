def solution(id_list, report, k):
    names = {value : 0 for value in id_list}
    answer = [0] * len(id_list)
    
    report = list(set(report))
    
    for i in report:
        names[i.split()[1]] += 1
    
    for i in report:
        x = i.split()[0]
        y = i.split()[1]
        if names[y] >= k:
            answer[id_list.index(x)] += 1
        
        
    return answer
        