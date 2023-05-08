def solution(lottos, win_nums):
    answer = []
    rank={'6':1,'5':2,'4':3,'3':4,'2':5,'1':6,'0':6}
    count1=0
    count2=0
    win=[]
    for i in lottos:
    # print('실제',i)
        if i in win_nums or i==0:
            count1+=1
#case2
    for j in lottos:
        if j in win_nums:
            count2+=1
    answer.append(str(count1))
    answer.append(str(count2))
    win.append(rank[answer[0]])
    win.append(rank[answer[1]])
    return win