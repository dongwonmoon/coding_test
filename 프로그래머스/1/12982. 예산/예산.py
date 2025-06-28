def solution(d, budget):
    answer = 0
    while d:
        min_ = min(d)
        d.remove(min_)
        budget -= min_
        answer += 1
        if budget < 0:
            answer -= 1
            break
    return answer