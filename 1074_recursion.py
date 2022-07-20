import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

# 문제가 재귀라고 판단이되면
# 우선 제일 먼저 최소 단위부터 생각해야한다.
# 2*2 모눈종이가 최소 단위인것을 생각해야한다.

# 이제 이 최소 단위까지 재귀로 코드를 보내는 생각을하면된다.

# z모양으로 탐색하기 위해서 2*2사각형이 될때까지 재귀함수를 호출해야한다
# 사각형의 시작값과 길이를 넘겨주면된다.

# 재귀에 값을 보낼때 , (x, y, 사각형 크기 값) 을 보낸다.

n, r, c = map(int, input().split())
cnt = 0

def recursion(x, y, size):
    global cnt
    # 사이즈 최소단위가 2일 때가 끝임.
    if size == 2:
        if x == r and y == c:
            print(cnt)
            return
        cnt += 1
        # 순서대로

        if x + 1 == r and y == c:
            print(cnt)
            return
        cnt += 1

        if x == r and y + 1 == c:
            print(cnt)
            return
        cnt += 1

        if x + 1 == r and y + 1 == c:
            print(cnt)
            return
        cnt += 1
    
    else:
        recursion(x, y, size//2)
        recursion(x, y + size//2, size//2)
        recursion(x + size//2, y, size//2)
        recursion(x + size//2, y + size//2, size//2)

recursion(0, 0, 2**n)
