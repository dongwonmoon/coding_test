def solution(numbers, target):
    count = 0
    
    def dfs(i, s):
        nonlocal count
        if i == len(numbers):
            if s == target:
                count += 1
            return
        
        dfs(i+1, s+numbers[i])
        dfs(i+1, s-numbers[i])
    
    dfs(0, 0)
    return count