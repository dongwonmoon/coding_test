def solution(n, m, section):
    n = list(range(1, n+1))
    for s in section:
        n[s-1] = 0
    
    count = 0
    i = 0
    while i < len(n):
        if n[i] == 0:
            count += 1
            i += m
        else:
            i += 1
        
    return count