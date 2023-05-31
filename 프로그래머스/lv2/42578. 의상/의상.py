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
        res=res*(k+1)#아무것도 없는 경우도 있으니까 1을 더해서 경우의 수 계산
    return res-1

#의상 핵심
#의상이 뭔지는 중요하지않다 가지고 있는 의상의 종류만을 가지고 경우의 수만 구하면 되는문제
#여기서 경우의수를 구할때 하나만 입어도된다고 했으니까 아무것도 입지 않는 경우의수를 옷에다 1을 더하고 계산
#https://velog.io/@hamham/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%EC%9C%84%EC%9E%A5 그림 자료 참고
