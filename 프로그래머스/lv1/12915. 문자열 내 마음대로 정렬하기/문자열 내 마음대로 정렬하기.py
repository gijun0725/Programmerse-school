def solution(strings, n):
    strings.sort() 
    return sorted(strings, key=lambda x:x[n])
#나중에 한번더 보면 좋은 풀이 key를 함수화 해서 정렬하는 방법인데 매우 유용하다 
