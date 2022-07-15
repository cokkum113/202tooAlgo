import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

anslist = []
mini = 10000000001

lo = 0
hi = n - 1

# 우선 이렇게 hi를 뒤에서 부터 줄이면서 와야한다는 생각과 아 우선, sorting할 생각을 하지 못했다.
# 포인터를 움직일때 sort할 생각을 하지 못했다. 
nums.sort()
total = nums[lo] + nums[hi]

# 또한 abs로만 해결을 하려고 했던 것도 문제였다. 

while lo < hi:
    # if lo == hi:
    #     break

    if abs(total) < mini:
        mini = abs(total)
        anslist.append([nums[lo], nums[hi]])
    
    if total == 0:
        anslist.append([nums[lo], nums[hi]])
        break

    elif total > 0:
        # 0에 더 가까워져야하니까 lo를 +시켜야한다
        # 음수 + 양수 인데 0보다 큰 값이니까 양수 쪽을 줄인다.  
        total -= nums[hi]
        hi -= 1
        total += nums[hi]

    elif total < 0:
        # 0보다 작을 때는 음수쪽이 크니까 음수의 인덱스를 올린다. 
        total -= nums[lo]
        lo += 1
        total += nums[lo]
    
    

if anslist:
    print(' '.join(map(str, anslist[-1])))