def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    twices = [word + word for word in words]
    
    for bab in babbling:
        FLAG = False
        for twice in twices:
            if twice in bab:
                FLAG = True
        if not FLAG:
            for word in words:
                bab = bab.replace(word, " ")
            if "".join(bab.split(" ")) == "":
                answer += 1
    return answer