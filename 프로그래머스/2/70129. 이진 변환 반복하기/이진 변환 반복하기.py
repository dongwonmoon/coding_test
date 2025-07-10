def solution(s):
    count = 0
    tries = 0
    while s != "1":
        count += s.count("0")
        c = len(s.replace("0", ""))
        b = []
        while c > 0:
            b.append(c % 2)
            c //= 2
        s = "".join(reversed(list(map(str, b))))
        tries += 1
        
    return [tries, count]