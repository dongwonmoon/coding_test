def solution(n, w, num):
    row = (num - 1) // w
    col = (num - 1) % w
    
    if row % 2 == 0:
        col_true = col
    else:
        col_true = w - 1 - col

    total_rows = (n + w - 1) // w 
    last_len = n - w * (total_rows - 1) # 맨 위층 남은 수

    below = total_rows - row
    
    if last_len < w: # 짤린 경우
        last_layer_idx = total_rows - 1
        if last_layer_idx % 2 == 0: # 왼->오
            if col_true > last_len - 1:
                below -= 1
        else: # 오 -> 왼
            if col_true < w - last_len:
                below -= 1

    return below
