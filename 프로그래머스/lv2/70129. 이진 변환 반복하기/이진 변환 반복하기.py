def solution(s):
    answer = []
    zero=0
    count=0
    while(s!='1'):
        zero+=s.count('0')
        s=bin(len(s.replace('0','')))[2:]
        count+=1
    answer.append(count)
    answer.append(zero)
    return answer