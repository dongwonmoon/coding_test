import operator

def solution(N, stages):
    stage_dict = {}
    stages.sort()
    for stage in range(1, N+1):
        challengers = len(list(filter(lambda x: x >= stage, stages)))
        del stages[:len(stages) - challengers]
        if challengers == 0:
            stage_dict[stage] = 0
        else: 
            fail = stages.count(stage)
            stage_dict[stage] = fail / challengers
    
    return [x[0] for x in sorted(stage_dict.items(), key=operator.itemgetter(1, 1), reverse=True)]