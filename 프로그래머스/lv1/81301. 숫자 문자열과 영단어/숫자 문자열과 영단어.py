def solution(s):
    dic={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    answer = []
    ex=''
    for i in range(len(s)):
        if s[i].isdigit()==True:
            answer+=s[i]
        else:
            ex+=s[i]
            if ex in dic:
                answer+=dic[ex]
                ex=''
            else:
                pass
    
    return int(''.join(answer))
#이 문제의 핵심 dic를 통해서 키와 벨류값을 잘 얻어올수 있는지 추가적으로 isdigit을 쓸줄 아는지에 대한 문제라고 생각한다
#카카오 문제 치고 어렵지 않았음
