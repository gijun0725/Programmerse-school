def solution(number):
    answer = 0
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            for e in range(j+1,len(number)):
                if(number[i]+number[j]+number[e])==0:
                    answer+=1
    return answer
