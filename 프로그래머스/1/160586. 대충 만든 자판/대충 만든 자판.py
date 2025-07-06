def solution(keymaps, targets):    
    short_cut = {}
    for keymap in keymaps:
        for i, key in enumerate(keymap):
            og = short_cut.get(key, 999)
            short_cut[key] = i + 1 if og > i + 1 else og
    
    answer = []
    for target in targets:
        push = 0
        for key in target:
            count = short_cut.get(key, -1)
            if count == -1:
                push = -1
                break
            push += count
        answer.append(push)
        
    return answer
    