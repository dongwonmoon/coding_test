def solution(n):
    f = [0, 1]
    for _ in range(n):
        f.append(f[-2] + f[-1])
        
    return f[-2] % 1234567