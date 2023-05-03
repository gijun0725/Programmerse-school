def solution(n, arr1, arr2):
    answer = []
    result = ''
    answer = []

    for one, two in zip(arr1, arr2):
        answer1 = '{0:0>{1}}'.format(bin(one)[2:], n)
        answer2 = '{0:0>{1}}'.format(bin(two)[2:], n)
        line = ''
        for i in range(n):
            if answer1[i] == '1' or answer2[i] == '1':
                line += '#'
            else:
                line += ' '
        answer.append(line)
    print(answer)
    return answer

#비밀 지도에서의 핵심 정리
#1.{0:0>{1}}'.format(bin(one)[2:] one에 들어가는 숫자를 bin을 통하여 이진수로 만들어 [2:]로 앞에
#접두어를 삭제
#{0:0>{1}}이부분에서 1에 n의 변수가 들어가고 n이 만약 6이라면 문자가 6자리가 될 때까지 0을 앞에 추가햊ㅁ
#ex)'010'인경우 ->'000010'으로 만들어 주는 역할
#이와 비슷한 방식은 rjust()방식이 있다 이는 만약 name=alice이고 
#name.rjust(10)이 되는경우 문자열의 길이가 10이 될때까지 문자열을 오른쪽으로 밀면서 공백을 추가한다
