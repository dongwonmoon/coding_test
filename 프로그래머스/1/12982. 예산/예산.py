def solution(d, budget):
    d.sort()
    answer = 0
    for price in d:
        if budget - price >= 0:
            budget -= price
            answer += 1
        else:
            break
    return answer
