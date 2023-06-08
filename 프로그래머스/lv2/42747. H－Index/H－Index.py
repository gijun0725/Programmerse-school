def solution(citations):
    citations.sort(reverse= True)
    answer = 0
    for H_idx in range(len(citations)):

        if citations[H_idx] > H_idx:
            answer = H_idx +1
        else:
            return answer

    return answer
