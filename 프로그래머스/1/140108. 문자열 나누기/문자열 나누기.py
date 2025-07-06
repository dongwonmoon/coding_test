def solution(s):
    splited = []
    
    x = ""
    counts = [0, 0]
    idx = 0
    for i, ch in enumerate(s):
        if x == "":
            x = ch
            idx = i
            
        if x == ch:
            counts[0] += 1
        else:
            counts[1] += 1
            
        if counts[0] == counts[1]:
            x = ""
            counts = [0, 0]
            splited.append(s[idx:i+1])
        elif sum(counts) > 0 and i == len(s) - 1:
            splited.append(s[idx:])
            
    return len(splited)