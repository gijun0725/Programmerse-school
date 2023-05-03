def solution(t, p):
    answer = 0
    z=len(p)
    for i in range(len(t)):
        if (len(t[i:i+z])==z) and (int(t[i:i+z])<=int(p)):
            answer+=1

    return answer