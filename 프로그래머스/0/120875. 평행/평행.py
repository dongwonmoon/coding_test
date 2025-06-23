def solution(dots):
    pos_sets = [[0, 1, 2, 3], [0, 2, 1, 3], [0, 3, 1, 2]]
    slopes = []
    
    for sets in pos_sets:
        pair1 = dots[sets[0]], dots[sets[1]]
        pair2 = dots[sets[2]], dots[sets[3]]
        
        slope1 = abs((pair1[1][1] - pair1[0][1]) / (pair1[1][0] - pair1[0][0]))
        slope2 = abs((pair2[1][1] - pair2[0][1]) / (pair2[1][0] - pair2[0][0]))
        
        if slope1 == slope2:
            return 1
    return 0