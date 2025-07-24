def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        count = 0
        if progresses[0] >= 100:
            for i in range(len(progresses)):
                if progresses[i] >= 100:
                    count += 1
                else:
                    break
            for _ in range(count):
                del progresses[0]
                del speeds[0]
            answer.append(count)
        
    return answer