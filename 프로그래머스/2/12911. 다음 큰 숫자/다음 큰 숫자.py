def solution(n):
    ones = format(n, "b").count("1")
    n += 1
    while format(n, "b").count("1") != ones:
        n += 1
        
    return n