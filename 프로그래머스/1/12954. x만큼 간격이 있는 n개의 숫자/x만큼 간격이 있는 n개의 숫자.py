def solution(x, n):
    answer = []
    a = x
    while len(answer) < n:
        answer.append(a)
        a += x
        
    return answer