def solution(N, stages):
    from collections import Counter

    stage_counts = Counter(stages)
    total = len(stages)
    result = []

    for stage in range(1, N + 1):
        if total == 0:
            result.append((stage, 0))
        else:
            fail = stage_counts.get(stage, 0)
            fail_rate = fail / total
            result.append((stage, fail_rate))
            total -= fail

    result.sort(key=lambda x: (-x[1], x[0]))
    return [stage for stage, _ in result]
