def solution(numbers):
    answer = ''
    a=list(map(str,numbers))
    sort=sorted(a,key=lambda x: x*3, reverse=1)
    return str(int("".join(sort)))


#내용 참고
먼저 주어진 숫자 리스트 numbers를 문자열 리스트 s로 바꿔줍니다. 
그리고 정렬을 해주는데, key=lambda x: x*3을 이용해 역순으로 정렬해 줍니다.
이는 "3" 과 "32"의 비교에서 "333"과 "323232"의 비교를 역순으로 하는 것입니다.
사전 순으로 따지면 "333"이 뒤에 나오며, 역순이니 앞에 나오게 됩니다.
즉, 정렬 결과 a는 더 큰 숫자 문자열이 앞에 나오는 내림차순으로 정렬됩니다.
여기서 문자열 리스트를 join 해서 int로 바꾸고 str 취해서 반환합니다.
여기서 int로 바꾸고 str로 변환하는 이유는 a에 ["0", "0"]에 대해 int를 취해주지 않으면 "00"으로 반환됩니다.
문제는 이를 "0"으로 반환하고 싶으므로 str(int("00")) 이렇게 하면, "0"으로 반환됩니다.
