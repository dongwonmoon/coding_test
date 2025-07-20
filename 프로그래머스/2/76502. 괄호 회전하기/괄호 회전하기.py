def solution(s):
    s = " ".join(s).split(" ")
    count = 0
    def check_wrong(check):
        q = []
        for c in check:
            q.append(c)
            if len(q) > 1 and (q[-2] + q[-1] in ["()", "{}", "[]"]):
                q.pop()
                q.pop()
        if q == []:
            return True
        else:
            return False
        
    for i in range(len(s)):
        check = s[i:]
        if check_wrong(check):
            count += 1
            
        s.append(s[i])
    
    return count