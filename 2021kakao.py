import sys
input = sys.stdin.readline

new_id = input()

def step_one(new_id):
    new_id2 = ''
    for i in new_id:
        if 'A' <= i <= 'Z':
            n = ord(i) + 32
            i = chr(n)
            new_id2 = new_id2 + i
        else:
            new_id2 = new_id2 + i
    
    return new_id2

def step_two(new_id):
    new_id2 = ''
    for i in new_id:
        if 'a' <= i <= 'z' or '0' <= i <= '9' or i == '-' or i == '_' or i == '.':
            new_id2 = new_id2 + i
        else:
            new_id2 = new_id2 + ''
    
    return new_id2

def step_three(new_id):
    for i in range(1, len(new_id)):
        if new_id[i] == '.' and new_id[i - 1] == '.':
            new_id[i] = ""
            new_id[i - 1] = '.'

    
    return new_id

def step_4(new_id):
    new_id2 = ""
    # if new_id[0] == '.':

    # if new_id[-1] == '.':
    #     print("dfsdfs")
    return new_id2

print(step_one(new_id))