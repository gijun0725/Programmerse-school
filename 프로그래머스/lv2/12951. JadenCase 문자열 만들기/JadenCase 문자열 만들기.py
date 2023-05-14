def solution(s):
    answer = ''
    if s[0].isalpha()==True:
            print(s[0])
            answer+=s[0].upper()
    else:
        answer+=s[0]
    for i in range(1,len(s)):
        try:
            if s[i-1]==' ' and s[i].isalpha()==True:
                print(s[i])
                answer+=(s[i].upper())
            else:
                answer+=(s[i].lower())
        except:
            pass
            
    
    return answer