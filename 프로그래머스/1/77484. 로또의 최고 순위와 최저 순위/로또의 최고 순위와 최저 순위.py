# 0이 이미 구매한 번호와 겹치면 안됨.
def solution(lottos, win_nums):
    rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5}
    hit = set(win_nums) & set(lottos)
    
    return [rank.get(lottos.count(0) + len(hit), 6), rank.get(len(hit), 6)]
    