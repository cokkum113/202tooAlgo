def solution(n, times):
    answer = 0
    lo = 1
    hi = int(1e21)
    while lo <= hi:
        total = 0
        mid = (lo + hi) // 2
        
        for t in times:
            total += mid // t
            
        if total >= n:
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return answer