def find_pre(l, w):
    if w in l:
        idx = l[::-1].index(w)
        return idx + 1
    else:
        return -1

def solution(s):
    answer = []
    l = []
    for w in s:
        answer.append(find_pre(l, w))
        l.append(w)
    return answer