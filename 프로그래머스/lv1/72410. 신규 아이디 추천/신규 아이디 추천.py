import re
def solution(new_id):
    answer = ''
    new_ids=''
    for i in range(len(new_id)):
        if new_id[i].isupper()==True:
            new_ids+=new_id[i].lower()
        else:
            new_ids+=new_id[i]
    comp = re.compile('[^-_.\w]+')
    new_ids=comp.sub('',new_ids)
    comp=re.compile('\.{2,}')  # '.' 문자가 2개 이상 연속되는 패턴을 정의합니다.
    new_ids = comp.sub('.', new_ids)
    new_ids = new_ids.strip('.')
    new_ids=new_ids.strip('.')
    if len(new_ids)==0:
        new_ids+='a'
    if len(new_ids)>15:
        new_ids=new_ids[:15]
    while len(new_ids)<=2:
        new_ids+=new_ids[-1]
    new_ids = new_ids.strip('.')
    new_ids=new_ids.strip('.')
    
    return new_ids
