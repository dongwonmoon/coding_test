def solution(elements):
    len_elements = len(elements)
    elements = elements * 2
    
    sums = []
    for length in range(1, len_elements+1):
        for i in range(len(elements)):
            sums.append(sum(elements[i:i+length]))
            
    return len(set(sums))