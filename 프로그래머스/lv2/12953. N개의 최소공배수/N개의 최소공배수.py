def solution(arr):
    answer = 0
    m=max(arr)
    while True:
        c=0
        for i in arr:
            if m%i ==0:
                c+=1
            else:
                break
        if c==(len(arr)):
            break
        m+=1
    return m