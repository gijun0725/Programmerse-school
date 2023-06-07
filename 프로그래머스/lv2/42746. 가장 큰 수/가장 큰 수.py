def solution(numbers):
    answer = ''
    a=list(map(str,numbers))
    sort=sorted(a,key=lambda x: x*3, reverse=1)
    return str(int("".join(sort)))