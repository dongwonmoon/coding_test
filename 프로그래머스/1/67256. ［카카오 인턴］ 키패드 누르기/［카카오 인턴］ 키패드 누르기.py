def solution(numbers, hand):
    result = []
    key_map = [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               ["*", 0, "#"]]
    key_index = {e: [row_i, col_i] for row_i, row in enumerate(key_map) for col_i, e in enumerate(row)}
    position = [[3, 0], [3, 2]]
    
    for number in numbers:
        key = key_index[number]
        if number in [1, 4, 7]:
            result.append("L")
            position[0] = key
            continue
        elif number in [3, 6, 9]:
            result.append("R")
            position[1] = key
            continue        
        else:
            left_dist = abs(position[0][0] - key[0]) + abs(position[0][1] - key[1])
            right_dist = abs(position[1][0] - key[0]) + abs(position[1][1] - key[1])

            if left_dist < right_dist:
                result.append("L")
                position[0] = key
            elif left_dist > right_dist:
                result.append("R")
                position[1] = key
            else:
                if hand == "right":
                    result.append("R")
                    position[1] = key
                else:
                    result.append("L")
                    position[0] = key
                
    return "".join(result)
    