def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        i_list = []
        for p, q in zip(i, j):
            i_list.append(p + q)
        answer.append(i_list)
    return answer