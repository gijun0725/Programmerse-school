def solution(sizes):
    answer1=[]
    answer2=[]
    for i in range(len(sizes)):
        sizes[i].sort()
        answer1.append(sizes[i][0])
        answer2.append(sizes[i][1])

    return max(answer1)*max(answer2) 