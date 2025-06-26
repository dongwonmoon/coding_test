def solution(n):
    answer = ""
    watermelon = ("수", "박")
    i = 0
    while n > 0:
        i %= 2
        answer += watermelon[i]
        i += 1
        n -= 1
        
    return answer