def solution(nums):
    answer = 0
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for e in range(j+1,len(nums)):
                num=(nums[i]+nums[j]+nums[e])
                # print(num)
                min=0
                for ex in range(2,num):
                    if num%ex==0:#나누어 떨어지면 소수가 아님
                        min+=1
                if min==0:
                    answer+=1
    return answer

#소수 만드는 방법의 핵심
#num숫자를 끝점으로 하여 2부터 num전가지 1씩 증가하면서 0으로 나누어 떨어지는 경우 소수로 판단 하지 않는다
#위 코드에서는 한번이라도 나누어 떨어지게 된다면 소수로 판단하지 않는다
