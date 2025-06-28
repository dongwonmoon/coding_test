def solution(s):
    answer = ''
    s = s.lower()
    
    i = 0
    for w in s:
        if w == " ":
            i = -1
        if i % 2 == 0:
            answer += w.upper()
        else: 
            answer += w
        i += 1
    return answer