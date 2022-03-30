#k번째 수
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        #50 
        i, j, k = commands[i]
        new_arr = array[i - 1: j]

        new_arr.sort()
        #100
        answer.append(new_arr[k - 1])
    return answer

    # 500 _ 1초가 안됨

#가장 큰 수 #시초뜨는거 
def solution(numbers):
    answer = ''
    nums = {}
    for i in numbers:
        x = i % 10
        nums[i] = x
    
    nums = sorted(nums.items(), key= lambda x : x[1], reverse=True)
    
    for i in nums:
        answer += str(i[0])
    
    
    
    return answer

#가장 큰수 시초뜨는거
def solution(numbers):
    answer = ''
    nums = []
    
    for i, val in enumerate(numbers):
        #100000
        x = val % 10
        nums.append([str(x), i])

    nums.sort(key = lambda x : x[0], reverse= True)
    #Reverse하면 시간이 100000 * 100000 인가용? 그러면 10 ^ 10으로 시초 뜨는 건가요?
    #이 방식은 3번째 방식으로 밖에 못 푸나용?
    
    for i in nums:
        #100000
        answer += str(numbers[i[1]])
    
    return answer

#가장 큰 수 
def solution(numbers):
    answer = ''
    nums = [str(x) for x in numbers]
    nums.sort(key=lambda x : x * 3, reverse=True)
    answer = str(int(''.join(nums)))
    return answer
########이 방법 말고는 없는지



# H - index
def solution(citations):
    a = len(citations)
    citations.sort()
    for i in range(a):
        if citations[i] >= a - i:
            return a - i
    return 0
    
    