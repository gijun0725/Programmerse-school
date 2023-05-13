def solution(babbling):
    answer = 0
    for i in babbling:
        for j in [ "aya", "ye", "woo", "ma" ]:
            if j * 2 not in i:#2개 곱한게 안에 ex)aya aya는 안에 들어있으니까 안지운다  "ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"] 이리스트 안에서 있으니까 
                i = i.replace(j, ' ')#i는 만약 ayaye 인기준에서 
        if len(i.strip()) == 0:
            answer += 1
    return answer