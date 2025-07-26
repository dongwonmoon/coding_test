from collections import defaultdict

def solution(phone_book):
    hash_set = set()
    
    for p in phone_book:
        for i in range(1, len(p)):
            hash_set.add(p[:i])
    
    for p in phone_book:
        if p in hash_set:
            return False
        
    return True