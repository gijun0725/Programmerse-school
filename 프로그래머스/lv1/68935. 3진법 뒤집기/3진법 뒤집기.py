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