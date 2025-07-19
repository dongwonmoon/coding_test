def solution(want, number, discount):
    want_dict = {w: n for w, n in zip(want, number)}
    count = 0
    
    for i in range(len(discount)):
        l = discount[i: i+10]
        
        tmp = []
        for w in want:
            if want_dict.get(w, None) != None and l.count(w) >= want_dict.get(w, None):
                tmp.append(1)
        if len(tmp) == len(want) and all(tmp):
            count += 1
            
    return count