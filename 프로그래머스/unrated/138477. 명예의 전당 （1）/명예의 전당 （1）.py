def solution(k, score):
    answer = []
    sortlist=[]
    for i in score:
        sortlist.append(i)
        sortlist.sort()
        answer.append(sortlist[-k:][0])
    return answer