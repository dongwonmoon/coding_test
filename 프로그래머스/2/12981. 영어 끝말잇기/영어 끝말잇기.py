def solution(n, words):
    q = []
    for i, word in enumerate(words):
        if q:
            if word in q or q[-1][-1] != word[0]:
                return [(i % n) + 1, i // n + 1]
        q.append(word)
        
    return [0, 0]