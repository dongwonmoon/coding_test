def solution(array):
    elem_count = dict()
    for elem in array:
        elem_count[elem] = array.count(elem)
        
    sorted_count = sorted(elem_count.items(), key=lambda x: x[1], reverse=True)
    print(sorted_count)
    if len(sorted_count) > 1:
        if sorted_count[0][1] == sorted_count[1][1]:
            return -1
        else:
            return sorted_count[0][0]
    else:
        return sorted_count[0][0]