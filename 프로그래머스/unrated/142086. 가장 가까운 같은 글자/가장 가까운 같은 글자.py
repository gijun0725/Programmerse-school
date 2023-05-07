def solution(s):
    answer = []
    s=list(s)
    for i in range(len(s)):
        if s[i] in s[:i]:#t앞에 t랑 같은게 있다면
            answer.append(i - s.index(s[i]))#자신의 인덱스 - 앞에나온 인덱스
            s[s.index(s[i])]=''#앞에있는거 중복일경우가 있어서 삭제
        else:
            answer.append(-1)
    return answer