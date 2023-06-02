def solution(s):
    answer = 0
    for i in range(len(s)):
        a=s
        for _ in range(len(a)):
            if a:
                a=a.replace('()','')
                a=a.replace('{}','')
                a=a.replace('[]','')
        if not a:
            answer+=1
        s=s[1:] +s[0]
            
    return answer