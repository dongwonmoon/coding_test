def solution(a, b):
    min_ = min(a, b)
    max_ = max(a, b)
    return sum(list(range(min_, max_+1)))