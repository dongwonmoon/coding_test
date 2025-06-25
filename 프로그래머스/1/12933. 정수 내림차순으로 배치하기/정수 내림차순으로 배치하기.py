def solution(n):
    sort = sorted([e for e in str(n)])
    reverse = reversed(sort)
    
    return int("".join(reverse))