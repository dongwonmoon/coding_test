def solution(citations):
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        h = i + 1
        if citations[i] < h:
            return i
    return len(citations)