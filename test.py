# def solution(A, B):
#     A = str(A)
#     B = str(B)
#     x = B.find(A)

#     return x

# def solution(A):
#     s = [A[0]]
#     cnt = 0
#     mini = 100001
    
#     for i in range(1, len(A)):
#         while s:
#             if s[-1] <= mini:
#                 mini = s[-1]
#                 break
#             else:
#                 cnt += 1
#                 s.pop()
#         s.append(A[i])      
#     return cnt

def solution(A):
    
    cnt = 0
    mini = 100001
    A = A[::-1]
    
    for i in A:
        if i <= mini:
            mini = i
            cnt += 1
    return cnt

# print(solution([2, 1, 3, 5, 4]))
# print(solution([2, 3, 4, 1, 5]))
print(solution([1, 3, 4, 2, 5]))
        

# from collections import defaultdict
# def solution(S):
#     city = defaultdict(list)
#     citycnt = defaultdict(int)
#     S = list(S.split('\n'))
#     for i in S:
#         a = i.split(', ')[0]
#         photoId = i.split('.')[0]
#         a = a.split('.')[1]
#         cityName = i.split(', ')[1]
#         date = str(i.split()[2])
#         date = date.replace("-","")
#         time = str(i.split()[3])
#         time = date.replace(":","")
#         alltime = date+time
#         city[cityName].append([alltime, photoId,a])
#         citycnt[cityName] += 1
    
#     sorted(city.items(), key=lambda x : x[1])
#     photoNumber = defaultdict()
#     for i in citycnt:
#         x = citycnt[i]
#         if len(str(x)) == 1:
#             photoNumber[i] = 1
#         elif len(str(x)) == 2:
#             photoNumber[i] = 2
#         elif len(str(x)) == 3:
#             photoNumber[i] = 3

#     # print(photoNumber)
#     anslist = []
    
#     for i in photoNumber:
#         cnt = 0
#         for j in city[i]:
#             if photoNumber[i] == 1:
#                 ans = i + str(cnt + 1) + '.' + j[2]
#                 cnt = cnt + 1
#                 anslist.append(ans)
#             if photoNumber[i] == 2:
#                 if cnt < 9:
#                     ans = i + str(0) + str(cnt + 1) + '.' + j[2]
#                     cnt = cnt + 1
#                     anslist.append(ans)
#                 else:
#                     ans = i + str(cnt + 1) + '.' + j[2]
#                     cnt = cnt + 1
#                     anslist.append(ans)
                    
#             if photoNumber[i] == 3:
#                 if cnt < 9:
#                     ans = i + str(0) + str(0) + str(cnt + 1) + '.' + j[2]
#                     cnt = cnt + 1
#                     anslist.append(ans)
#                 elif cnt < 99:
#                     ans = i + + str(0) + str(cnt + 1) + '.' + j[2]
#                     cnt = cnt + 1
#                     anslist.append(ans)
#                 else:
#                     ans = i + str(cnt + 1) + '.' + j[2]
#                     cnt = cnt + 1
#                     anslist.append(ans)
#     print('\n'.join(anslist))
#     return anslist

                
            
        


        
        

        
