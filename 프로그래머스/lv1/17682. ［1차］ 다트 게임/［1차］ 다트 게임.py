def solution(dartResult):
    i = 0
    n = len(dartResult)
    scores = []
    while i < n:
        if dartResult[i].isdigit() and dartResult[i + 1].isdigit():
            score = int(dartResult[i:i + 2])
            bonus = dartResult[i + 2]
            i += 3
        else:
            score = int(dartResult[i])
            bonus = dartResult[i + 1]
            i += 2
        if bonus == 'S':
            pass
        elif bonus == 'D':
            score **= 2
        elif bonus == 'T':
            score **= 3
        scores.append(score)
        if i < n:
            if dartResult[i] == '*':
                scores[-1] *= 2
                if len(scores) > 1:
                    scores[-2] *= 2
                i += 1
            elif dartResult[i] == '#':
                scores[-1] *= -1
                i += 1
    return sum(scores)
