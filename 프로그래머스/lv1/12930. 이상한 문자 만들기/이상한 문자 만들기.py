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

#문제의 핵심
#주어진 test 케이스가 너무 쉬웠기에 금방 할 줄 알았지만 실제 테스트시에 거의 대부분 실패였다
#실패의 이유는 다음과 같다 -> 공백이 당연히 하나인줄 알았지만 두개 이상 이라는 말이 있었고
#맨뒤에 공백을 무시하면 안되고 다시 만들어줘야한다 즉 split할때 공백을 기준으로 날리지말고 최대한 살려야 했다
