def solution(n, m, section):
    answer = painted = 0
    for i in section:
        if i>=painted:
            painted=i+m
            answer+=1
    return answer
#덧칠하기 핵심 시작 painted=0부터 만약 i(section)이 나왔을때 칠해진 부분과 크거나 같다면 페인트 칠을 해야하니까
#painted = i(section)부터 m(롤러길이) 만큼 칠하고 painted된 영역을 업데이트 해주고 한번칠했으니 answer를 업데이트 하면된다
