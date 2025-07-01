def solution(answers):
    sp_1 = list(range(1, 6))
    sp_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    sp_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    sps = [sp_1, sp_2, sp_3]
    scores = [0, 0, 0]
    
    for i, sp in enumerate(sps):
        window = len(sp)
        for j in range(0, len(answers), window):
            answer = answers[j:j+window]
            for s, a in zip(sp, answer):
                if s == a:
                    scores[i] += 1
    
    submit = []
    max_ = max(scores)                
    ind_sc = {i: score for i, score in enumerate(scores)}
    for i, score in ind_sc.items():
        if score == max_:
            submit.append(i+1)
            
    return sorted(submit)