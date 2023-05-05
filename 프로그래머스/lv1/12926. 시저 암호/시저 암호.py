def solution(s, n):
    answer = ''
    alpha1="abcdefghijklmnopqrstuvwxyz"
    alpha2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in s:
        print(i)
        if  i in alpha1:
            ind= (alpha1.find(i)+n)
            answer+=alpha1[ind%len(alpha1)]

        elif i in alpha2:
            ind=(alpha2.find(i)+n)
            answer+=alpha2[ind%len(alpha2)]
        else:
            answer+=' '
    return answer