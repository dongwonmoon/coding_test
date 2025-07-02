from itertools import combinations

def solution(nums):
    max_ = sum(sorted(nums)[-3:])
    combs = combinations(nums, 3)
    
    s = set(range(2, max_+1))
    for i in range(2, max_+1):
        s -= set(range(i*2, max_+1, i))
    
    count = 0
    for comb in combs:
        if sum(comb) in s:
            count += 1
            
    return count