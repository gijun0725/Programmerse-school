def solution(N, stages):
    answer = []
    result=[]
    counts = [0 for i in range(N+2)]
    total_players = len(stages)
    
    for stage in stages:
        counts[stage] += 1
    
    for i in range(1,N+1):
        if total_players == 0:
            fail_rate = 0
        else:
            fail_rate = counts[i] / total_players
            total_players -= counts[i]
        answer.append((i, fail_rate))
    
    answer.sort(key=lambda x: -x[1])
    
    for stage in answer:
        result.append(stage[0])
    
    return result
