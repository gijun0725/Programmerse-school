def solution(n):
    answer = 0
    if n<3:
        return n
    else:
        ans=[0]*(n+1)#ans 배열 생성 
        ans[1],ans[2]=1,2
        for i in range(3,n+1):
            ans[i]=ans[i-1]+ans[i-2]
    return ans[n]%1234567