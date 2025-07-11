def solution(s):
    q = []
    for c in s:
        q.append(c)
        
        if len(q) >= 2:
            if q[-2] == q[-1]:
                q.pop()
                q.pop()
                
    return 1 if len(q) == 0 else 0