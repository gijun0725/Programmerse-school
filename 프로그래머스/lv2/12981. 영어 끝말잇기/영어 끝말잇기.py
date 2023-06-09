def solution(n, words):
    answer = [0,0]
    stack=[]
    cnt=0
    stack.append(words[0])
    for i in range(1,len(words)):
        cnt+=1
        if words[i] not in stack and (words[i-1])[-1] ==(words[i])[0]:
            stack.append(words[i])
        else:
            answer[0]=cnt%n +1
            answer[1]=cnt//n + 1
            break
    

    return answer