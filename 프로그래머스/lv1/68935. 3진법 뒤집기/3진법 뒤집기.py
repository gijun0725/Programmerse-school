def solution(n):
    answer = ''
    answers=0
    while(n>0):
        extra=n%3
        n=n//3
        answer+=str(extra)
    answer=str(answer)[::-1]
    for i in range(len(answer)):
        answers+=int(answer[i])*int(3**i)
    return answers
#3진법 계산 방법만 안다면 쉽게 가능하다 굳이 핵심이라 하면 3**i를 통해서 i가 증가함에 다라 제곱의 수가 바뀌는것만 캐치한다면 쉬웠을 것이다
