from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
visited = [False] * len(nums)

ans = []
aa = []
cc = []
def backtracking(index):
    ############ans를 리턴할때 값이 안사라지게 하려면 deepcopy말고 뭘 써야할지 
    if len(ans) == m:
        aa = deepcopy(ans)
        if aa not in cc:
            cc.append(aa)
        return
        
    for i in range(1, len(nums) + 1):
        if visited[i - 1] == False:
            ans.append(nums[i - 1])
            visited[i - 1] = True
            backtracking(index + 1)
            ans.pop()
            visited[i - 1] = False
        else:
            continue

backtracking(0)

for i in cc:
    print(*i)