import re
def solution(s):
    answer = ''
    number=re.compile('[-\d]+')
    nums=number.findall(s)
    nums.sort(key=int)
    answer+=nums[0] +' '+nums[-1]
    return answer