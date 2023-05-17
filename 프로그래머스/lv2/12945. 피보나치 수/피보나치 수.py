def solution(n):
    answer = 0
    answer=[0,1]
    for i in range(2,n+1):
        answer.append((answer[i-2]+answer[i-1])%1234567)
    return answer[-1]
#피보나치수는 이전값을 가져와서 활용해야 하기 때문에 배열에 하나씩 추가해서 i-2부터 다시 가져오면 값을 계속 이용할 수 있다
