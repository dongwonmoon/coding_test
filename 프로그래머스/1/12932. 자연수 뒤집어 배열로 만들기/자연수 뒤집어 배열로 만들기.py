def solution(n):
    return list(map(int, "".join(str(n)[::-1])))