def solution(n, arr1, arr2):
    answer = []
    result = ''
    answer = []

    for one, two in zip(arr1, arr2):
        answer1 = '{0:0>{1}}'.format(bin(one)[2:], n)
        answer2 = '{0:0>{1}}'.format(bin(two)[2:], n)
        line = ''
        for i in range(n):
            if answer1[i] == '1' or answer2[i] == '1':
                line += '#'
            else:
                line += ' '
        answer.append(line)
    print(answer)
    return answer