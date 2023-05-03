def solution(s):
    answer = ''
    s=s.replace(' ','.')
    s=s.split('.')
    text=''
    for i in range(len(s)):
        for j in range(len(s[i])):#3,5 이런식으로간다
            # print(s[i][j])
            if s[i][j]==' ':
                text+=' '

            if j%2==0:
                text+=s[i][j].upper()
            else:
                text+=s[i][j].lower()
        if i<len(s)-1:
            text+=' '
    return text