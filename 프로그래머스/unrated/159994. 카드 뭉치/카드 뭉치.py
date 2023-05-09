def solution(cards1, cards2, goal):
    answer = []
    n=len(cards1)
    m=len(cards2)
    i=j=0
    for word in goal:
        if i<n and word==cards1[i]:
            answer.append(cards1[i])
            i+=1
        if j<m and word==cards2[j]:
            answer.append(cards2[j])
            j+=1
    return 'Yes' if answer==goal else 'No'

#카드 뭉치의 핵심은 두개의 i,j를 따로 접근하면서 하나씩 증가시키는 방법이다
#보통 for문을 이용해서 두개를 접근했는데 for문에만 집착하다보니 간단한 방법을 어떻게 구현하는지 까먹었다
#접근방법은 맞았으나 코드로 구현하는걸 실패했던 문제 다시한번 풀면 맞는다
