from collections import defaultdict
def solution(record):
    answer = []
    id_list = []
    
    names = defaultdict(list)
    for i in record:
        if i.split()[0] != 'Leave':
            user = i.split()[1]      
            nickname = i.split()[2]
            id_list.append(user)
            names[user].append(nickname)
    # print(names)
    for i in record:
        # if i.split()[0] == 'Change':
        #     continue
        if i.split()[0] == 'Leave':
            x = names[i.split()[1]][-1]
            answer.append(x+"님이 나갔습니다.")
        elif i.split()[0] == 'Enter':
            x = names[i.split()[1]][-1]
            answer.append(x+"님이 들어왔습니다.")
            
    # print(answer)
    return answer