import sys
input = sys.stdin.readline

n, c = map(int, input().split())

#10^6으로 백트래킹 불가.다른 방법으로 해야함

home = []
for _ in range(n):
    home.append(int(input()))

home.sort()

# 설치할수 있는 거리를 확인해야함
st = 1
# 차이가 1에서 시작
end = home[-1] - home[0]
# 가장 차이 많이 날때

ans = 0

while st <= end:
    mid = (st + end) //2
    cnt = 1
    #처음 부터 카운트되게 하기 mid (사이거리)를 조절하면서

    current_pos = home[0]
    mini = int(1e9)

    for i in range(1, len(home)):
        if mid + current_pos <= home[i]:
            cnt += 1
            mini = min(mini, home[i] - current_pos)
            current_pos = home[i]
    
    if cnt >= c:
        # 설치해야하는 것보다 더 크다는 것은 거리를 넓혀서 적게 설치하자는 뜻
        st = mid + 1
        #답은 여기에
        ans = max(mini, ans)
    elif cnt < c:
        end = mid - 1
        # 원래 갯수보다 적다는 것는 거리를 좁혀서 많이 설치하자는 뜻
print(ans)