import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
visited = [False] * 4
nums = [1, 5, 10, 50]
cnt = [0] * (20 * 50 + 1)
num = 0

def bt(index, st):
    global num
    if index == n:
        # 인덱스는 지금 어느 깊이까지 들어왔는지
        # 이게 n까지 들어온거면 return 해야함
        cnt[num] = 1
        return
    
    for i in range(st, 4):
        num += nums[i]
        bt(index + 1, i)
        num -= nums[i]
            
bt(0, 0)
print(sum(cnt))
