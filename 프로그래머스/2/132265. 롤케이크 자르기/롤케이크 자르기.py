from collections import Counter, defaultdict

def solution(topping):
    answer = 0
    if len(set(topping)) == len(topping):
        return 1
    
    l = defaultdict(int)
    r = Counter(topping)
    for t in topping:
        l[t] += 1
        r[t] -= 1
        if r[t] == 0:
            r.pop(t)
        if len(l) == len(r):
            answer += 1
        
    return answer