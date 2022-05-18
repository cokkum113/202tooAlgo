import sys
input = sys.stdin.readline

##############96퍼에서 틀림#####################

# 가장 가까운수 조합을 찾기
# 그러면 차이를 미니멈값으로 두고 그 차이가 작을때 값을 딕셔너리로 저장하면될거같다
# 수빈이가 지금 보고 있는 채널은 100!!!!!!



n = int(input())
m = int(input())
if m != 0:
    broken = list(map(int, input().split()))
elif n != 100 and m == 0:
    print(len(str(n)))
    exit(0)

diff = int(1e9)
#100에서 +, - 로 이동했을때랑
diff = min(diff, abs(100 - n))

if n == 100:
    print(0)
    exit()

# 숫자 입력해서 +, - 갈때, 숫자 입력해서가는거는 숫자를 누르냐 마느냐니까
#숫자의 len()을 더해주면 될거같음
#+, - 누를떄를 생각해야해서 두번더하기
for channel in range(1000001):
    yyy = str(channel)
    for i in range(len(yyy)):
        if int(yyy[i]) in broken:
            break
        elif len(yyy) - 1 == i:
            diff = min(diff, len(yyy) + abs(channel - n))

print(diff)