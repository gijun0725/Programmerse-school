def solution(clothes):
    answer = 0
    cloth_list=[]
    for i in clothes:
        cloth_list.append(i[1])
    dictlist={}
    for j in cloth_list:
        dictlist[j]=cloth_list.count(j)
    res=1
    for k in dictlist.values():
        res=res*(k+1)
    return res-1