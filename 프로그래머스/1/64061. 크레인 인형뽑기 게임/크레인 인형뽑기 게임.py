def solution(board, moves):
    stack = []
    count = 0
    for move in moves:
        for i in range(len(board)):
            doll = board[i][move-1]
            if doll != 0:
                stack.append(doll)
                board[i][move-1] = 0
                break
                      
    stack2 = []
    for s in stack:
        stack2.append(s)
        if stack2[-2:] == [s] * 2:
            stack2.pop()
            stack2.pop()
            count += 1
                        
    return count * 2