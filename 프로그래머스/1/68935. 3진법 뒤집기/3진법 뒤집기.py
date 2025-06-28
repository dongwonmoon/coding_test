def solution(n):
    digit_3 = []
    while n > 0:
        digit_3.append(str(n % 3))
        n /= 3
        n = int(n)
    return int("".join(digit_3), 3)