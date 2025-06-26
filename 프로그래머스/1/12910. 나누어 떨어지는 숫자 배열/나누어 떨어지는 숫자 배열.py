def solution(arr, divisor):
    answer = sorted(list(filter(lambda x: x % divisor == 0, arr)))
    
    if answer:
        return answer
    else:
        return [-1]