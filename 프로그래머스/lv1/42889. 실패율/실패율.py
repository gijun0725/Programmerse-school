def solution(N, stages):
    answer = []
    result=[]
    counts = [0 for i in range(N+2)]#0으로 배열 생성
    total_players = len(stages)#8개까지가능하다고 하면  players는8이다
    
    for stage in stages:
        counts[stage] += 1
    
    for i in range(1,N+1):
        if total_players == 0:
            fail_rate = 0
        else:
            fail_rate = counts[i] / total_players# 첫번재는 0/8, 두번째는 1/8, 세번째는 3/(8-1) 네번째는 2/(7-3).... 
            total_players -= counts[i]
        answer.append((i, fail_rate))#배열에 접근해서 추가해준다 [(3, 0.5), (4, 0.5), (2, 0.42857142857142855), (1, 0.125), (5, 0.0)] 팁!: 추가할때 인덱스랑 값이랑 묶어서 배열에 추가할 수 있다 참고하기 
    
    answer.sort(key=lambda x: -x[1])#정렬할때는 순서는 필요하지않고 값만 필요하니까 값기준으로 정렬하면 숫자도 같이 따라간다 ->매우 좋은 방법
    
    for stage in answer:
        result.append(stage[0])#정렬했으니 순서의 기준으로 나열하면 된다 
    
    return result

#실패율 최종요약
#가장 관건은 시간복잡도였다 아래의 기존 풀이가 있었다 테스트 케이스는 무리없이 통과했고 실제 테스트에서 거의 다 맞았지만 
#몇개의 시간복잡도를 해결하지 못했다
#첫번째로 해결한 방법은 counts의 값을 미리 저장해 두는 방법을 통해서 메모리를 최대한 사용하지 않았다

1번 해결방법
================================================================================================================
counts = [0 for i in range(502)]
for i in range(len(stages)):
    counts[stages[i]] += 1
counts[i] # stages.count(i)와 동일한 결과
---------------------------------------------------------------------
해결방법[처음에 사용하지 않은 이유는 0이 추가되어서 처리하기 불편해서 사용하지 않음]
for stage in stages:#stages를 접근하면서 해당 숫자 배열에 1씩 더한다
        counts[stage] += 1
        print(counts)#최종출력은 0부터 n까지 count
================================================================================================================

for i in range(1,N+1):
    # print(stages.count(i))
    count=0
    num=0
    for j in range(len(stages)):
        if stages[j]>=i:
            count+=1
    print('stage:{} num:{} count:{} counts:{}'.format(i,num,count,counts[i]))
    answer.append(counts[i]/count)
for _ in range(N):
    # print(answer.index(max(answer)))
    result.append(answer.index(max(answer))+1)
    answer[answer.index(max(answer))]=-1
