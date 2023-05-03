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
#정석적인 풀이는 아니지만 리스트 형태로 반복되는것을 미리 표현한다음 answer의 길이만큼 같이 늘어나야하니까 answer길이를 계속 늘려주고 zip을 통해서 동시에 접근하였다
