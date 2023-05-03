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