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
    
    