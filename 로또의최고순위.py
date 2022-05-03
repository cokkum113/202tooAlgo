def solution(lottos, win_nums):
    answer = []
    
    original_cnt = 0
    for i in lottos:
        if i in win_nums:
            original_cnt += 1
    print(original_cnt)
    
    zero = lottos.count(0)
    print(zero)
    
    ans = 0
    total = zero + original_cnt
    ans1 = 0
    if original_cnt == 6:
        ans1 = 1
        answer.append(ans1)
    elif original_cnt == 5:
        ans1 = 2
        answer.append(ans1)
    elif original_cnt == 4:
        ans1 = 3
        answer.append(ans1)
    elif original_cnt == 3:
        ans1 = 4
        answer.append(ans1)
    elif original_cnt == 2:
        ans1 = 5
        answer.append(ans1)
    else:
        ans1 = 6
        answer.append(ans1)
    #total은 더하는 것
    if total == 6:
        ans = 1
        answer.append(ans)
    elif total == 5:
        ans = 2
        answer.append(ans)
    elif total == 4:
        ans = 3
        answer.append(ans)
    elif total == 3:
        ans = 4
        answer.append(ans)
    elif total == 2:
        ans = 5
        answer.append(ans)
    else:
        ans = 6
        answer.append(ans)
    print(answer)
    answer.sort()
    return answer