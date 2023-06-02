def solution(s):
    answer = True
    stack=[]
    for i in range(len(s)):
        if s[0]==')':
            return False
        elif s[i]=='(':
            stack.append(s[i])
        else:
            if stack:
                stack.pop()
    if stack:
        answer=False

    return answer