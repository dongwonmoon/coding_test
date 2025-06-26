def solution(num):
    if num == 1:
        return 0
    
    count = 0
    while count < 500 and num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        num = int(num)
        count += 1
        
    if count >= 500:
        return -1
    return count