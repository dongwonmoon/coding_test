def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    
    for i in range(0, len(score) - len(score) % m, m):
        box = score[i:i + m]
        answer += min(box) * m
        
    return answer