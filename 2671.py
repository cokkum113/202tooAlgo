import sys
input = sys.stdin.readline


# 잠수함 엔진 소리가 아닐 때를 판별하면됨

# 1뒤에 1이 올때 그뒤가 또 1이오면 안됨
def check_one(s):
    for i in range(len(s) - 2):
        if s[i] == '1' and s[i + 1] == '0' and s[i + 2] == '1' and s[i + 3] :
            return False
    return True


s = input().rstrip()
if check_one(s):
    print("SUBMARINE")
else:
    print("NOISE")