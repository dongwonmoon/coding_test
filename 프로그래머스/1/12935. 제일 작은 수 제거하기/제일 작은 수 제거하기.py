def solution(arr):
    min_ = min(arr)
    arr.remove(min_)
    if arr:
        return arr
    else:
        return [-1]