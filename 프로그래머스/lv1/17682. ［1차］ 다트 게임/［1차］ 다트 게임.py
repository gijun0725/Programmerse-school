def solution(dartResult):
    i = 0
    n = len(dartResult)
    scores = []
    while i < n:
        if dartResult[i].isdigit() and dartResult[i + 1].isdigit():
            score = int(dartResult[i:i + 2])
            bonus = dartResult[i + 2]
            i += 3
        else:
            score = int(dartResult[i])
            bonus = dartResult[i + 1]
            i += 2
        if bonus == 'S':
            pass
        elif bonus == 'D':
            score **= 2
        elif bonus == 'T':
            score **= 3
        scores.append(score)
        if i < n:
            if dartResult[i] == '*':
                scores[-1] *= 2
                if len(scores) > 1:
                    scores[-2] *= 2
                i += 1
            elif dartResult[i] == '#':
                scores[-1] *= -1
                i += 1
    return sum(scores)

#다트게임 정규표현식 풀이 방법 [정규표현식의 필요성]
import re
dartResult='1S2D*3T'
bonus={'S':1, 'D':2, 'T':3}
option={'':1, '*':2, '#':-1}

p=re.compile('(\d+)([SDT]),([*#]?)')#이 정규표현식을 컴파일 하는 이유는 
#여기서 \d+의 +는 여러글자가 들어와도 된다 즉 1회이상 반복될때 사용한다
#[SDT]는 + 가없기 때문에 단일문자만 Return된다 만약 [SDT]+가 있다면 단일문자는 Return되지않고 SSDTS,DTTTS와 같은 문자가 반환된다
#[*#]? 이부분은 ?가 중요하다 *#문자가 한번 등잘할수 있거나 등장하지 않을수도 있다는 의미이다
#dartResult가 들어왔을때 search, match, findall, sub 과 같은 기능을 앞에 붙이기만 하면되기 때문이다
dart=p.findall(dartResult)#이처럼 p에 정규표현식을 컴파일 해두고 findall과 같이 기능만 앞에 적어주면 된다
for i in range(len(dart):
               if dart[i][2]=='*' and i>0:
                    dart[i-1]*=2#앞에나온 결과에도 *2를 해줘야한다 findall하면 리스트로 반환되니까 리스트 각원소에 *2만 해주면 된다
               dart[i]=int(dart[i][0])**bonus[dart[i][1]]*option[dart[i][2]]
#dart=[2,8,27]이런식으로 반환된다
               #최종결과는 sum(dart)
                
