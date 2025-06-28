def solution(s):
    answer = ''
    ords = []
    for w in s:
        ords.append(ord(w))
    ords.sort(reverse=True)
    for o in ords:
        answer += chr(o)
    return answer