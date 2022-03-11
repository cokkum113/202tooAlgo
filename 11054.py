import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums2 = nums[::-1]

increase = [1] * n
decrease = [1] * n
ans = [0] * n

for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if nums2[i] > nums2[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)
    

for i in range(n):
    ans[i] = increase[i] + decrease[n - i - 1] - 1
print(max(ans))

