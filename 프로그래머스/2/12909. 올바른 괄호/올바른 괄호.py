def solution(s):
    ps = []
    for p in s:
        ps.append(p)
        if len(ps) >= 2:
            if ps[-2] == "(" and ps[-1] == ")":
                ps.pop()
                ps.pop()
                
    return True if len(ps) == 0 else False