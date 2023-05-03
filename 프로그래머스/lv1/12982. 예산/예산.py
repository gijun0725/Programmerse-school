def solution(d, budget):
    answer = 0
    d=list(sorted(d))
    for i in range(len(d)):
        print(budget,d[i],i)
        budget-=d[i]
        
        if budget<0:
            answer=i
            break
        else:
            answer=i+1
    return answer