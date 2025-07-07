def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_map = {"code":0, "date": 1, "maximum":2}
    ext = ext_map.get(ext, 3)
    
    for d in data:
        if d[ext] < val_ext:
            answer.append(d)
            
    return sorted(answer, key=lambda x: x[ext_map.get(sort_by, 3)])