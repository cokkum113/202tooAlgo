import sys
input = sys.stdin.readline
n = int(input())

heap = [-1] * 100001
heap_size = 0
def push(x):
    global heap
    global heap_size
    heap_size += 1
    heap[heap_size] = x
    parent = heap_size//2
    child = heap_size
    
    while(child > 1) and (heap[child] > heap[parent]):
        heap[child], heap[parent] = heap[parent], heap[child]
        child = parent
        parent = child
def pop():
    global heap
    global heap_size
    result = heap[1]
    heap[1] = heap[heap_size]
    heap[heap_size] = 0
    heap_size -= 1
    parent = 1
    child = 2
    #do-while
    if (child+1 <= heap_size) and (heap[child] < heap[child+1]):
        child = child + 1
    while (child <= heap_size) and (heap[parent] < heap[child]):
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent*2
        if (child+1 <= heap_size) and (heap[child] < heap[child+1]):
            child = child + 1
    return result

for i in range(n):
    node = int(input())
    if node == 0: 
        if heap_size > 0:
            ans = pop()
            print(ans)
        else:
            print(0)
    else:
        push(node)