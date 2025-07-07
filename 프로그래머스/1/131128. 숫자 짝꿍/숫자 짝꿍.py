from collections import Counter

def solution(X, Y):
    both = set(X) & set(Y)
    if both == set():
        return "-1"
        
    c_X = {num: count for num, count in Counter(X).items() if num in both}
    c_Y = {num: count for num, count in Counter(Y).items() if num in both}
    
    l = []
    for num in c_X.keys():
        x_num, y_num = c_X[num], c_Y[num]
        l += [num] * min(x_num, y_num)
    
    answer = "".join(sorted(l, reverse=True))
    if answer[0] == "0":
        return "0"
    else:
        return answer