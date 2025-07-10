def solution(n):
    count = 0
    p = list(range(1, n//2 + 2))
    
    for a in range(len(p)):
        for i in range(1, len(p)-a+1):
            if sum(p[a:a+i]) > n:
                break
            elif sum(p[a:a+i]) == n:
                count += 1
                break
    if n == 1 or n == 2:
        return 1
    else:
        return count + 1