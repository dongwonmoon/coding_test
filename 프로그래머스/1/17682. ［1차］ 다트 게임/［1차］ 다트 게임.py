import re

def solution(dartResult):
    results = []
    bonuses = re.split(r'\d+', dartResult)[1:] # Why [0] = ""?
    numbers = re.findall(r'\d+', dartResult)
    
    for number, bonus in zip(numbers, bonuses):
        p = 1 if "S" in bonus else 2 if "D" in bonus else 3
        results.append(int(number) ** p)
        
        if "*" in bonus:
            if len(results) >= 2:
                results[-2] *= 2
            results[-1] *= 2
        elif "#" in bonus:
            results[-1] *= -1
            
    return sum(results)