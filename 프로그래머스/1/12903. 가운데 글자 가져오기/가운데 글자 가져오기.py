def solution(s):
    if len(s) % 2 == 0:
        if len(s) == 2:
            return s
        sel = int(len(s) / 2)
        return s[sel-1:sel+1]
    else:
        if len(s) == 1:
            return s
        sel = int((len(s) + 1) / 2)
        return s[sel-1]