def solution(n, plans, clients):
    answer = []
    for cl in clients:
        cl = cl.split()
        want_giga = cl[0]
        want_service = cl[1:]
        aa = 0
      
        
        for index, t in enumerate(plans):
            t = t.split()
            giga = t[0]
            service = t[1:]
            if want_giga <= giga:
                for i in want_service:
                    if i not in service:
                        continue
                    else:
                        aa = index + 1
                            
                        
        answer.append(aa)

        
    return answer


#
# 입력값 〉
# 5, ["100 1 3", "500 4", "2000 5"], ["300 3 5", "1500 1", "100 1 3", "50 1 2"]
# 기댓값 〉
# [3, 3, 1, 0]

'''
입력값 〉
4, ["38 2 3", "394 1 4"], ["10 2 3", "300 1 2 3 4", "500 1"]
기댓값 〉
[1, 2, 0]
'''