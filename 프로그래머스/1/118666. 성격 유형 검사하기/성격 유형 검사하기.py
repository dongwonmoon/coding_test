def solution(survey, choices):
    choice_score = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    characters = [["R", "T"],
                  ["C", "F"],
                  ["J", "M"],
                  ["A", "N"]]
    scores = {character: 0 for row in characters for character in row}
    
    for i, s in enumerate(survey):
        choice = choices[i]
        score = choice_score[choice]
        if choice in [1, 2, 3]:
            scores[s[0]] += score
        else:
            scores[s[1]] += score
    
    mbti = []
    for row in characters:
        max_ = ""
        if scores[row[0]] > scores[row[1]]:
            max_ = row[0]
        elif scores[row[0]] < scores[row[1]]:
            max_ = row[1]
        else:
            max_ = row[0] if ord(row[0]) < ord(row[1]) else row[1]
        mbti.append(max_)
        
    return "".join(mbti)