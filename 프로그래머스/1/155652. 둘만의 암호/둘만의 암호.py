def solution(s, skip, index):
    alphabet = set([chr(x) for x in range(ord("a"), ord("z")+1)])
    alphabet -= set(skip)
    alphabet = sorted(list(alphabet))
    alphabet_dict = {a: i for i, a in enumerate(alphabet)}
    len_alphabet = len(alphabet)
    
    answer = []
    for a in s:
        answer.append(alphabet[(alphabet_dict[a]+index) % len_alphabet])
        
    return "".join(answer)