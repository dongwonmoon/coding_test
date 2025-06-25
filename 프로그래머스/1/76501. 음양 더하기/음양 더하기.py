def solution(absolutes, signs):
    signs = list(map(lambda x: 1 if x else -1, signs))
    return sum([absolutes[i] * signs[i] for i in range(len(absolutes))])