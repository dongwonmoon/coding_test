from collections import Counter, defaultdict

def make_list(s):
    l = []
    for i in range(len(s)):
        w = s[i:i+2]
        if len(w) == 2 and w.isalpha():
            l.append(w)
    return l

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    s1 = make_list(str1)
    s2 = make_list(str2)
    
    if s1 == s2 and s1 == []:
        return 65536
    
    s1 = Counter(s1)
    s2 = Counter(s2)
    
    a1 = s1 if len(s1) < len(s2) else s2
    a2 = s1 if a1 == s2 else s2
    
    inter = defaultdict(int)
    uni = defaultdict(int)
    for s in a1:
        if s in a2:
            inter[s] = a1[s] if a1[s] < a2[s] else a2[s]
        uni[s] = a1[s]
    for s in a2:
        uni[s] = a2[s]
        if s in a1:
            uni[s] = a2[s] if a2[s] > a1[s] else a1[s]
            
    return 65536 * sum(inter.values()) // sum(uni.values())