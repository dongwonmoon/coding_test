def solution(sizes):
    # 가로 보다 세로가 더 길면서 세로가 max인 놈
    sizes.sort(reverse=True, key=lambda x: x[1])
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i] = [sizes[i][1], sizes[i][0]]
    
    sizes_w, sizes_h = [size[0] for size in sizes], [size[1] for size in sizes]
    
    return max(sizes_w) * max(sizes_h)