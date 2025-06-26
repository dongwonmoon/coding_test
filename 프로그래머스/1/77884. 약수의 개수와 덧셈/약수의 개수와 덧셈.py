def get_count(a, b):
    div_counts = dict()
    for i in range(a, b+1):
        for j in range(1, i+1):
            if i % j == 0:
                count = div_counts.get(i, 0)
                div_counts[i] = count + 1
    return div_counts
                
def solution(left, right):
    div_counts = get_count(left, right)
    ll = []
    
    for key, value in div_counts.items():
        if value % 2 == 0:
            ll.append(key)
        else:
            ll.append(-key)
            
    return sum(ll)