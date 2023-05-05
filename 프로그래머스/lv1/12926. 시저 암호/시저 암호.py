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
#시저암호 문제 핵심 내용
#isalpha도 있지만 find도 있다 find는 리스트가아닌 문자열에서 s라는 글자가 어디에있는지 인덱스 값을 반환환한다
#순서대로 반복되는경우 전체 길이에서 인덱스를 나누어주면 그위치가 반환된다 그걸 이용하면 풀 수 있다
