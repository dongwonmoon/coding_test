def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for w in words:
            b = b.replace(w, " ", 1)
        if b.replace(" ", "") == "":
            answer += 1
    return answer