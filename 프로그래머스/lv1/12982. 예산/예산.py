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
#이 문제의 핵심 최대 지원 가능한 부서의 횟수를 구해야하는데 부서를 기준으로 계산하는것이 아니다
#핵심은 예산이 초과되기 전까지 지원가능한 회사의 개수이니 예산에서 금액을 계속 빼고 예산 이 초과되기 직전에 부서의 수를 계산한다
#만약 초과되지 않는다면 전체 부서의 수가 최대 지원 가능한 부서이다
#예산에서 부서를 빼는것을 생각하지 못한다면 시간이 오래 걸릴 것 으로 예상
