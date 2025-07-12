from collections import Counter
def solution(k, tangerine):
    count = 0
    for v in sorted([v for v in Counter(tangerine).values()], reverse=True):
        count += 1
        k -= v
        if k <= 0:
            break
            
    return count