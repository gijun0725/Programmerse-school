import re
def solution(s):
    answer = ''
    number=re.compile('[-\d]+')
    nums=number.findall(s)
    nums.sort(key=int)
    answer+=nums[0] +' '+nums[-1]
    return answer

#핵심 정규표현식으로 공백제거
#sort에서 key로 int 지정하면 숫자 크기 별로 정렬가능 
