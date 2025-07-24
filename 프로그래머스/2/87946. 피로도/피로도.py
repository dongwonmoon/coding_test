from itertools import permutations

def solution(k, dungeons):
    count = -100
    for p in permutations(dungeons, len(dungeons)):
        kk = k
        d_count = 0
        for dungeon in p:
            if kk < dungeon[0]:
                break
            
            kk -= dungeon[1]
            d_count += 1
        
        if count < d_count:
            count = d_count
            
    return count