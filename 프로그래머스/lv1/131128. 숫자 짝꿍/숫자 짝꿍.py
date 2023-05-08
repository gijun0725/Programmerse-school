def solution(X, Y):
    answer = ''
    # ★ 포인트1. 반복되는 숫자를 저장하기 위한 dictionary (key: 0 ~ 9)
    numx = {str(n):0 for n in range(10)}
    numy = {str(n):0 for n in range(10)}
    
    # X 문자열 하나씩 돌면서 카운트
    for x in X:
        numx[x] += 1
    
    # Y 문자열 하나씩 돌면서 카운트
    for y in Y:
        numy[y] += 1
    
    # ★ 포인트2. 9부터 0까지 반복문 돌기. sort를 안 하기 위함.
    #           짝꿍을 큰 수부터 더해가면 자동으로 제일 큰 수가 됨.
    for k in range(9, -1, -1):
        k = str(k)
        iternum = min(numx[k], numy[k])
        
        # ★ 포인트3. "000" -> "0"으로 만들어주기 위한 조건문
        if answer == '' and k == '0' and iternum != 0:
            return "0"
        
        # 실패 코드 #############################
        # for _ in range(iternum):             #
        #     answer = ''.join([answer, k])    #
        ########################################
        # 성공 코드 ★★★★★
        # '9'*3 = '999'가 되는 원리를 이용
        answer = ''.join([answer, k*iternum])  
        ########################################
    
    if answer == '':
        return "-1"
    else:
        return answer
    
    
  #=================================================================
기존풀이
    def solution(X, Y):
    answer = []
    X = sorted(X)
    Y = sorted(Y)
    for i in X:
        if i in Y:
            answer.append(i)
            del [Y[Y.index(i)]]
    if len(answer)==0:
        answer='-1'
    elif int(''.join(answer))==0:
        answer='0'
    else:
        answer.sort(reverse=True)
    answer=''.join(answer)

    return answer
