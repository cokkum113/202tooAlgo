from socket import NI_NUMERICSERV
import sys
input = sys.stdin.readline

numslist = []
n = int(input())
for _ in range(n):
    rr = list(map(int, input().split()))
    numslist.append(rr)

numslist = sorted(numslist, key=lambda x : x[0])

#dp니까 답을 저장해서 가면될거같음 아니면 시초 안걸릴 범위라서 백트래킹 가능할거 같음
anslist = [0] * n
# 얘는 부분 증가수열을 카운트하는 애

'''
cnt = 0
for i in range(n):
    for j in range(i):
        #지워지는 경우를 카운트해보기 
        if numslist[i][1] > numslist[j][1]:
            # 이렇게 되면 지워짐 , 이때 지워지는 것을 카운트해줌, 
            #근데 이게 갑자기  offset이 커지면 앞에있는 것을 지운상태라 
            # 성립이 안됨......
1 8
3 9
4 1
6 4
7 6
9 2
10 10 
내 논리대로라면 9 2에서 카운트가 안됨. 최대가 나옴
print(anslist)
지리는 문제입니다........대박................
뺴주니까 9 2가 나오면 답이 안됐었는데, 답이 위로 거슬러 올라갈 일이 없으니까
증가하는 수열을 빼주니까 답이 나온다............
'''
# 최소 값 = 전기줄 - 최대로 안겹칠때.
for i in range(n):
    for j in range(i):
        if numslist[i][1] > numslist[j][1]:
            if anslist[i] < anslist[j]:
                anslist[i] = anslist[j]
    
    anslist[i] += 1
print(n - max(anslist))

