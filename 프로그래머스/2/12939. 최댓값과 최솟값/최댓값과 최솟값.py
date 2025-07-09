def solution(s):
    s = s.split(" ")
    s = list(map(int, s))
    return " ".join([str(min(s)), str(max(s))])
    