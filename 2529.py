import sys
input = sys.stdin.readline

n = int(input())


ss = list(input().split())

visited = [False] * 10

mini = int(1e9)
maxi = 0

now_nums = []

def possible(k, i, now):
    if ss[i] == '<':
        return k < now
            # k는 num안에 있는 수
    else:
        return k > now

rr = ""
ans = []

def backtracking(index):
    global rr, mini, maxi
    if index == n + 1:
        rr = ''.join(map(str, now_nums))
        ans.append(rr)
        return
    # 현재 여기서 해야할 코드를 넣기
    for j in range(10):
        if visited[j] == False:
            if now_nums:
                if possible(now_nums[-1],index -1, j):
                    now_nums.append(j)
                else:
                    continue
            else:
                now_nums.append(j)
        
            visited[j] = True
            backtracking(index + 1)
            visited[j] = False
            now_nums.pop()
        
backtracking(0)
print(ans[-1])
print(ans[0]) 