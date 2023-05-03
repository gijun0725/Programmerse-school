def solution(answers):
    answer = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    clist = []
    for i in range(len(answer)):
        count = 0
        for ex, re in zip(answer[i]*len(answers), answers):
            if ex == re:
                count += 1
        clist.append(count)
    
    max_count = max(clist)
    winners = [i + 1 for i, count in enumerate(clist) if count == max_count]
    
    return winners
