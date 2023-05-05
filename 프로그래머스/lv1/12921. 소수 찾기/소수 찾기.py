def solution(n):
    num=set(range(2,n+1))#n이 100이라면 100까지 나열
    for i in range(2,n+1):#i는 2부터 증가
        if i in num:#만약 2이라면 는 num안에 속함 
            num-=set(range(2*i,n+1,i))#핵심 아이디어 배수들은 모두 삭제한다 i는 2부터 10까지 증가 
            #2*2부터 10+1 즉 10까지 2씩 증가
            #3인경우 2*3 10까지 3칸씩 증가 
    return len(num)